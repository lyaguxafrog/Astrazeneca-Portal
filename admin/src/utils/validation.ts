export const required = (value: any, error = 'Поле обязательно для заполенения') => {
  if (Array.isArray(value)) {
    return !value.length ? error : true;
  }

  if (value) {
    return true;
  }

  return error;
};
