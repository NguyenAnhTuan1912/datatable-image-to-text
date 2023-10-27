// Import from components
import { ImageUpload } from "./components/image_upload/ImageUpload.js";

// Định nghĩa hàm main
/**
 * Hàm main
 * @param {HTMLDivElement} app 
 * @param utils 
 */
export function main(app, utils) {
  const fup = new ImageUpload(app, utils);

  // Thêm fup vào trong app
  fup.render();
}