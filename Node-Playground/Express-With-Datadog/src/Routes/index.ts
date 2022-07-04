import { Request, Response, Router } from "express";

import UserController from "../Controllers/UserController";
import { cacheRedis } from "../server";

const userController = new UserController();

const routes = Router();

routes.get("/", (request: Request, response: Response) => {
  return response.status(200).json({ message: "Hello Dev" });
});

routes.post("/users", userController.createUsers);
routes.get(
  "/users",
  cacheRedis.route({ name: "/users" }),
  userController.getUsers,
);
routes.get("/users/:id", cacheRedis.route(), userController.getUser);
routes.put("/users/:id", userController.updateUser);
routes.delete("/users/:id", userController.deleteUser);

export default routes;
