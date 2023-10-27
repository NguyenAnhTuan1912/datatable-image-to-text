import { createHandler } from '../templates/handler/index.js';

export const BlurImageHandler = createHandler(
  "/blur_image",
  function({ Utils }) {
    return function(req, res) {
      try {
        let body = req.body;
        console.log("Body: ", body);

        return Utils.RM.responseJSON(
          res,
          200,
          Utils.RM.getResponseMessage(false, "Hello", "Create post successfully.")
        );
      } catch (error) {
        return Utils.RM.responseJSON(
          res,
          500,
          Utils.RM.getResponseMessage(true, undefined, error.message)
        );
      }
    }
  }
);