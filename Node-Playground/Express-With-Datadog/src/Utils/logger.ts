import pino from "pino";
import "dotenv/config";

const levels = {
  http: 10,
  debug: 20,
  info: 30,
  warn: 40,
  error: 50,
  fatal: 60,
};

const log = pino({
  enabled: true,
  transport: {
    target: "pino-pretty",
    options: {
      colorize: true,
      levelFirst: true,
      messageFormat: true,
      translateTime: true,
    },
  },
  useOnlyCustomLevels: true,
  timestamp: true,
  customLevels: levels,
  level: "http",
});

export const logger = log;
