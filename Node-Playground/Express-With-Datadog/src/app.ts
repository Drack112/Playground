import { app } from "./server";
import { createLogger, format, transports } from "winston";

const loggerDatadog = createLogger({
  level: "info",
  exitOnError: false,
  format: format.json(),
  transports: [
    new transports.File({
      filename: `/home/drack/Documentos/Express-With-Datadog/logs/logs.log`,
    }),
  ],
});

const PORT = process.env.PORTA || 3000;

app.listen(PORT, () => {
  loggerDatadog.info("Log e DogData funcionando š¶");
  console.log(
    "š Express App has been started\nš Link -> http://localhost:" + PORT,
  );
});

export { app };
