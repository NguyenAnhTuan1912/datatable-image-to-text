// import { UtilsType } from "../utils/index.js";

export class ImageUpload {
  /**
   * 
   * @param {HTMLDivElement} app 
   * @param {UtilsType} utils 
   */
  constructor(app, utils) {
    this.app = app;
    this.utils = utils;
    this.ref = null;
  }

  _createContainer() {
    // Tạo input file element
    let imageFileHTML = `<input class="form-control form-control-lg" name="image" id="imageFile" type="file">`;

    let imageFile = this.utils.Element.toElement(imageFileHTML);

    // Tạo form
    let form = this.utils.Element.createElement("form", {
      className: "image-uploader-form",
      content: imageFile
    });

    // Tạo container.
    let container = this.utils.Element.createElement("div", {
      className: "image-uploader-container p-5",
      content: form
    });

    return container;
  }

  render() {
    if(!this.ref) this.ref = this._createContainer();
    this.app.append(this.ref);
  }
}