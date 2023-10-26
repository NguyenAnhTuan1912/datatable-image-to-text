/**
 * @typedef CreateElementOptions
 * @property {string | undefined} className
 * @property {string | undefined} id
 * @property {string | undefined} content
 * @property {any} style
 * @property {{[key in keyof HTMLElementEventMap]: (e: any) => void} | undefined} eventListeners
 */

/**
 * @param {string} html
 * @returns 
 */
function toElement(html) {
  let div = document.createElement("div");
  div.innerHTML = html;
  return div.children[0];
}

/**
 * @param {keyof HTMLElementTagNameMap} type
 * @param {CreateElementOptions | undefined} options
 * @returns 
 */
function createElement(type, options) {
  let element = document.createElement(type);

  if(options) {
    if(options.className) element.classList.add(...options.className.split(" "));
    if(options.id) element.id = options.id;
    if(options.content) element.innerHTML = options.content;
    if(options.style) {
      let _style = options.style;
      for(let key in _style) if(_style[key] !== undefined || _style[key] !== null) element.style[key] = _style[key];
    };
    if(options.eventListeners) {
      let _listeners = options.eventListeners;
      for(let key in _listeners)
        element.addEventListener(key, _listeners[key]);
    };
  }

  return element;
}

export const _Element_ = {
  /**
   * Phương thức này sẽ chuyển chuỗi html sang một element. 
   */
  toElement,
  /**
   * Phương thức này dùng để build một HTMLElement
   */
  createElement
};