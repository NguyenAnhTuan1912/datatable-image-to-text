// Import from classes
import { Component } from "../../classes/Component.js";

// import { UtilsType } from "../../utils/index.js";

export class ImagePicker extends Component {
  /**
   * @param {HTMLDivElement} app 
   * @param {UtilsType} utils 
   */
  constructor(app, utils) {
    super(app, utils);
  }

  _createContainer() {
    // Tạo input file element
    let imageFileHTML = `<input class="form-control form-control-lg" name="image" id="imageFile" type="file">`;

    let imageFile = this.utils.Element.toElement(imageFileHTML);

    // Tạo container.
    let container = this.utils.Element.createElement("div", {
      className: "image-picker",
      content: imageFile
    });

    return container;
  }
}