// Import from classes
import { Component } from "../../classes/Component.js";

// Import from components
import { ImagePicker } from "../image_picker/ImagePicker.js";

// Import types
// import { UtilsType } from "../../utils/index.js";

export class BlurImage extends Component {
  /**
   * @param {HTMLDivElement} app 
   * @param {UtilsType} utils 
   */
  constructor(app, utils) {
    super(app, utils);
  }

  _createContainer() {
    // Tạo input
    let imgpker = new ImagePicker(this.app, this.utils);
    let strthRge = this.utils.Element.toElement(`
      <div class="mb-3">
        <label for="strength-range" class="form-label">Blur strength</label>
        <input
          type="range"
          class="form-range"
          min="1" max="20" step="1"
          id="strength-range"
          name="strength-range"
          oninput="this.nextElementSibling.value = this.value"
        >
        <output>11</output>
      </div>
    `);
    let submitBtn = `<button type="submit" class="btn btn-primary mt-3">Thực thi</button>`;

    let imgpkerRef = imgpker.getRef();

    // Tạo output
    let output = this.utils.Element.createElement("div", {
      className: "output"
    });

    // Tạo form
    let form = this.utils.Element.createElement("form", {
      className: "blur-image-form",
      content: [strthRge, imgpkerRef, submitBtn],
      eventListeners: {
        "submit": function(e) {
          e.preventDefault();

          const req = new XMLHttpRequest();
          let file = e.target["image"].files[0];
          
          req.open("POST", "http://localhost:3000/api/image/blur_image", true);
          req.onload = (event) => {
            console.log("Event: ", event);
          };

          req.send(file);
          
          output.innerHTML = "";
        }
      }
    });

    // Tạo container
    let container = this.utils.Element.createElement("div", {
      className: "blur-image-container",
      content: [form, `<h2 class="my-3">Kết quả</h2>`, output]
    });

    return container;
  }
}