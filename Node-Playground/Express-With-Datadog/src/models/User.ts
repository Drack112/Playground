import mongoose, { Schema, Model, Document } from "mongoose";

type UserDocument = Document & {
  name: string;
  email: string;
  password: string;
};

type UserInput = {
  name: UserDocument["name"];
  email: UserDocument["email"];
  password: UserDocument["password"];
};

const usersSchema = new Schema(
  {
    name: {
      type: Schema.Types.String,
      required: true,
    },
    email: {
      type: Schema.Types.String,
      required: true,
      unique: true,
    },
    password: {
      type: Schema.Types.String,
      required: true,
    },
    enabled: {
      type: Schema.Types.Boolean,
      default: true,
    },
  },
  {
    collection: "users",
    timestamps: true,
  },
);

const User: Model<UserDocument> = mongoose.model<UserDocument>(
  "User",
  usersSchema,
);

export { User, UserInput, UserDocument };
