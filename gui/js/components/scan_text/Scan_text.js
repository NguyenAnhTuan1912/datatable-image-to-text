// Import from classes
import { Component } from "../../classes/Component.js";

// Import from apis
import { ImageAPIs } from "../../apis/image/index.js";

// Import from components
import { ImagePicker } from "../image_picker/ImagePicker.js";

// Import types
// import { UtilsType } from "../../utils/index.js";

export class ScanText extends Component {
  /**
   * @param {HTMLDivElement} parent 
   * @param {UtilsType} utils 
   */
  constructor(parent, utils) {
    super(parent, utils);
  }

  _createContainer() {
    // Tạo input
    let imgpker = new ImagePicker(this.parent, this.utils);
    let select = this.utils.Element.toElement(`
      <div class="mb-3">
        <select class="form-select" name="color" aria-label="Default select example">
        <option selected>Loại Bảng</option>
        <option value="0">Normal</option>
        <option value="1">Only Horizontal Lines</option>
        <option value="2">Only Vertical Lines</option>
        <option value="3">Only Covered Border</option>
      </select>
      </div>
    `);
    let strthRge = this.utils.Element.toElement(``);
    let submitBtn = `<button type="submit" class="btn btn-primary mt-2">Quét</button>`;

    let imgpkerRef = imgpker.getRef();

    let imgpreview = '<div class="mb-3"><img src="https://www.elle.vn/wp-content/uploads/2017/07/25/hinh-anh-dep-1.jpg" width = 200px height = 200px></div>'
    // Tạo output
    let guide = this.utils.Element.createElement("div", {
      className: "scan-image-guide",
      children: `
        <div>
          <h3>Hướng dẫn</h3>
          <p>scan text là là quét văn bản dựa trên những điểm đặc trưng của chữ cái sau đó tạo ra bảng trên excel </p>
          <ol>
            <li>Ấn vào <strong>Choose File</strong>.</li>
            <li>Chọn một tấm ảnh muốn quét.</li>
            <li>Chọn loại bảng</li>
            <li>Chờ Backend thực thi. Sau khi thực thi xong thì sẽ có một popup Download hiện lên, lưu ảnh vào đâu đó.</li>
            <li>Mở ảnh trong folder vừa lưu và xem kết quả.</li>
          </ol>
        </div>
      `
    });

    // Tạo form
    let form = this.utils.Element.createElement("form", {
      className: "scan-image-form",
      children: [imgpkerRef,select, imgpreview, submitBtn],
      eventListeners: {
        "submit": function(e) {
          e.preventDefault();
          const formData = new FormData(e.target);
          const imageFile = e.target["image"].files[0];

          ImageAPIs
          .convertColorImageAsync(formData)
          .then(res => {
            // Chuyển binary thành base64.
            const url = window.URL.createObjectURL(new Blob([res], { type: imageFile.type }));

            // Tạo một thẻ a và gán base64 vào href cho thẻ a.
            // Set thuộc tính download và tự động tải về.
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', imageFile.name);
            document.body.appendChild(link);
            link.click();
          })

          // return false;
        }
      }
    });

    // Tạo container
    let container = this.utils.Element.createElement("div", {
      className: "scan-image-container",
      children: [guide, form]
    });

    return container;
  }
}