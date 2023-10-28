// Import api callers
import { ImageAPIs } from "./image/index.js";

const API_ROOT = "http://localhost:3000/api";

const IMAGE_ROOT = "/image";

/**
 * Bọc một api caller để truyền api root và một số thông tin quan trọng khác.
 * @param {(url: string, ...data: Array<any>) => Promise<any>} fn 
 * @returns 
 */
function wrapAPICaller(part, fn) {
  return async function(...args) {
    return await fn(API_ROOT + IMAGE_ROOT + part, ...args);
  }
}

// Cài đặt wrapper
for(let callerKey in ImageAPIs) {
  ImageAPIs[callerKey] = wrapAPICaller("/blur_image", ImageAPIs[callerKey]);
}

export {
  ImageAPIs
}