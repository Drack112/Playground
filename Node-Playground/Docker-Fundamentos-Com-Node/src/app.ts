import { app } from "./server";

import "dotenv/config";

const PORT = process.env.PORTA;

app.listen(PORT, () => {
  console.log(
    "š Express App has been started\nš Link -> http://localhost:" + PORT,
  );
});

export { app };
