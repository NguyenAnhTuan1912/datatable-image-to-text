import bodyParser from "body-parser";
import cors from "cors";

import { MyServer } from "./classes/MyServer.js";
import { ServerBuilder } from "./classes/ServerBuilder.js";

const myServer = new MyServer({ port: process.env.PORT || "3000" });
const builder = new ServerBuilder({ server: myServer });

builder.buildMiddleWare(cors({ origin: "*" }));
builder.buildMiddleWare(bodyParser.json());
builder.buildMiddleWare(bodyParser.urlencoded({ extended: true }));

// Khởi động server.
myServer.start();