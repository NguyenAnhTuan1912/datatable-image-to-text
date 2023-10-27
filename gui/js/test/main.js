// Import from components
import { BlurImage } from "../components/blur_image/BlurImageForm.js";
import { Tab } from "../components/tab/Tab.js";

// Định nghĩa hàm main
/**
 * Hàm main
 * @param {HTMLDivElement} app 
 * @param utils 
 */
export function main(app, utils) {
  const blrimg = new BlurImage(app, utils);
  const tab = new Tab(app, utils,
    [
      ["blur-image", { label: "Làm mờ ảnh", element: blrimg.getRef() }],
      ["to-grayscale", { label: "Chuyển đổi ảnh về ảnh xám", element: "<h1>Chuyển đổi ảnh về ảnh xám</h1>" }],
      ["face-recognition", { label: "Nhận diện khuôn mặt", element: "<h1>Nhận diện khuôn mặt</h1>" }]
    ]
  );

  // Thêm title cho app
  app.innerHTML = `
    <header>
      <h1>Test Section</h1>
      <div>
        <p>Đây là phần test để xem hệ thống hoạt động có đúng hay không? Hỗ trợ một số tính năng như sau:</p>
        <ol>
          <li>Làm mờ ảnh</li>
          <li>Chuyển đổi ảnh màu thành ảnh trắng đen</li>
          <li>Nhận diện khuôn mặt</li>
        </ol>
      </div>
    </header>

    <hr></hr>
  `;

  // Thêm một số thuộc tính cho app
  app.classList.add("p-5");

  // Thêm các components vào trong app
  tab.render({ title: "Chọn tính năng" });
}