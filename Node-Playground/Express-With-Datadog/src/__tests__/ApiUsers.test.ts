import request from "supertest";

import { logger } from "../Utils/logger";
import { app } from "../app";

describe("Users Endpoint Test", () => {
  beforeAll(() => {
    logger.warn("Testes Do Jest Rodando!");
  });

  afterAll(() => {
    logger.warn("Testes Do Jest sendo encerrado!");
  });

  it("Should be able to create a new user", async () => {
    const response = await request(app).post("/users").send({
      name: "TestName",
      email: "TestEmail@gmail.com",
      password: "TestPassword",
    });

    expect(response.status).toBe(201);
  });

  it("Should be able to get Users", async () => {
    const response = await request(app).get("/users");

    expect(response.status).toBe(200);
  });
});
