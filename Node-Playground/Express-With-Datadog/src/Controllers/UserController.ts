import crypto from "crypto";
import { Request, Response } from "express";

import { User, UserInput } from "../models/User";

class UserController {
  async createUsers(request: Request, response: Response) {
    const { name, email, password } = request.body;

    const hashPassword = (password: string) => {
      const salt = crypto.randomBytes(16).toString();

      // Hashing salt and password with 100 iterations, 64 length and sha512 digest
      return crypto
        .pbkdf2Sync(password, salt, 100, 64, `sha512`)
        .toString(`hex`);
    };

    if (!name || !email || !password) {
      return response.status(422).json({
        message: "The fields name, email and password are required",
      });
    }

    const userInput: UserInput = {
      name,
      email,
      password: hashPassword(password),
    };

    const userCreated = User.create(userInput);

    return response.status(201).json({ data: userCreated });
  }

  async getUsers(request: Request, response: Response) {
    const users = await User.find().sort("-createdAt").exec();

    return response.status(200).json(users);
  }

  async getUser(request: Request, response: Response) {
    const { id } = request.params;

    const user = await User.findOne({ _id: id });

    if (!user) {
      return response
        .status(404)
        .json({ message: `User with id "${id}" not found.` });
    }

    return response.status(200).json({ user });
  }

  async updateUser(request: Request, response: Response) {
    const { id } = request.params;
    const { name, email } = request.body;

    const user = await User.findOne({ _id: id });

    if (!user) {
      return response
        .status(404)
        .json({ message: `User with id "${id}" not found.` });
    }

    if (!name || !email) {
      return response
        .status(422)
        .json({ message: "The fields name and email are required" });
    }

    await User.updateOne({ _id: id }, { name, email });

    const userUpdated = await User.findById(id, { name, email });

    return response.status(200).json({ data: userUpdated });
  }

  async deleteUser(request: Request, response: Response) {
    const { id } = request.params;

    await User.findByIdAndDelete(id);

    return response.status(200).json({ message: "User deleted successfully." });
  }
}

export default UserController;
