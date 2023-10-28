/**
 * Dùng caller này để convert một tấm ảnh thành ảnh mờ.
 * @param {string} path 
 * @param {FormData} data 
 * @returns 
 */
async function convertBlurImageAsync(path, data) {
  const response = await fetch(
    path,
    {
      method: "post",
      body: data
    }
  );

  return response.json();
}

export const ImageAPIs = {
  convertBlurImageAsync
};