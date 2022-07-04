import "reflect-metadata";
import { ApolloServer } from "apollo-server";
import { buildSchema } from "type-graphql";

import "./database/connection";
import { VideoResolver } from "./resolvers/video/VideoRessolver";

async function bootstrap() {
  const schema = await buildSchema({
    resolvers: [VideoResolver],
  });
  const server = new ApolloServer({ schema });
  server.listen({ port: 3000 }, console.log("🚀 Server running!"));
}

bootstrap();
