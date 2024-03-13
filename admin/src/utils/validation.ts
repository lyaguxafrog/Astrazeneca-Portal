function isUrlValid(str: string) {
  const pattern = new RegExp(
    '^(https?:\\/\\/)?' + // protocol
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
      '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR IP (v4) address
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
      '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
      '(\\#[-a-z\\d_]*)?$', // fragment locator
    'i'
  );
  return pattern.test(str);
}

export const required = (value: any, error = 'Поле обязательно для заполенения') => {
  if (Array.isArray(value)) {
    return !value.length ? error : true;
  }

  if (value) {
    return true;
  }

  return error;
};

export const isUrl = (value: any, error = 'Невалидный url') => {
  if (typeof value !== 'string') {
    return error;
  }

  if (isUrlValid(value) || value[0] === '/') {
    return true;
  }

  return error;
};
