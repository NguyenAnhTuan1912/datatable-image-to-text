// Import from classes
import { Component } from "../../classes/Component.js";

// Import from apis
import { ImageAPIs } from "../../apis/index.js";

// Import from components
import { ImagePicker } from "../image_picker/ImagePicker.js";

// Import types
// import { UtilsType } from "../../utils/index.js";

export class BlurImage extends Component {
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
      children: [strthRge, imgpkerRef, submitBtn],
      eventListeners: {
        "submit": function(e) {
          e.preventDefault();
          const formData = new FormData(e.target);
          
          ImageAPIs
          .convertBlurImageAsync(formData)
          .then(res => {
            e.preventDefault();
            console.log("Response: ", res);
          })

          // return false;
        }
      }
    });

    // Tạo container
    let container = this.utils.Element.createElement("div", {
      className: "blur-image-container",
      children: [form, `<h2 class="my-3">Kết quả</h2>`, output]
    });

    return container;
  }
}