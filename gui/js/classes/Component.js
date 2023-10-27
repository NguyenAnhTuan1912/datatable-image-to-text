export class Component {
  /**
   * @param {HTMLDivElement} app 
   * @param {UtilsType} utils 
   */
  constructor(app, utils) {
    /**
     * @type {HTMLDivElement}
     */
    this.app = app;
    /**
     * @type {UtilsType}
     */
    this.utils = utils;
    this.ref = null;
  }

  _createContainer() {}

  getRef() {
    if(!this.ref) this.ref = this._createContainer();
    return this.ref;
  }

  render() {
    if(!this.ref) this.ref = this._createContainer();
    this.app.append(this.ref);
  }
}