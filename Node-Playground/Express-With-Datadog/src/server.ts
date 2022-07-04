import "./tracer";

import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import express_pino from "express-pino-logger";
import cache from "express-redis-cache";

const cacheRedis = cache({
  host: "127.0.0.1",
  port: 6379,
  expire: 30,
});

import { logger } from "./Utils/logger";
import routes from "./Routes";
import "./database/connection";

import "dotenv/config";

const loggerMiddleware = express_pino({
  logger: logger,
  autoLogging: true,
  serializers: {
    req: (req) => ({
      method: req.method,
      url: req.url,
      user: req.raw.user,
      host: req.headers.host,
    }),
  },
});

const app = express();

app.use(bodyParser.json());
app.use(cors());
app.use(loggerMiddleware);
app.use(routes);

export { app, cacheRedis };
