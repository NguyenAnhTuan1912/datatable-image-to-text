// Import from components
import { ImagePicker } from "../components/image_picker/ImagePicker.js";

// Định nghĩa hàm main
/**
 * Hàm main
 * @param {HTMLDivElement} app 
 * @param utils 
 */
export function main(app, utils) {
  const m = utils.Element.createElement("div", {
    className: "p-3",
    children: `
      <div>
        <h2>Lưu ý</h2>
        <p>Hiện tại thì ứng dụng đang trong quá trình thử nghiệm, nên ae vào trong link bên dưới để qua Test Section nhé.</p>
        <a href="test.html">Chuyển qua Test section</a>
      </div>
    `
  });

  // Thêm fup vào trong app
  // imgpker.render();
  app.append(m);
}