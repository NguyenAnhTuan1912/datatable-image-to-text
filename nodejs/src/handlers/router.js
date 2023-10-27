import { createRouter } from '../templates/router/index.js';

// Import handlers
import { BlurImageHandler } from './blurImage.js';

const base = {
  image: "/image"
};

export const ImageRouter = createRouter({
  handlers: [
    {
      path: base.image + BlurImageHandler.path,
      method: "post",
      fns: [BlurImageHandler.handler]
    }
  ]
});