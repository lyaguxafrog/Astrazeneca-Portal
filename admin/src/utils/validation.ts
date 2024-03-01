export const required = (value: string | number, error = 'Поле обязательно для заполенения') => {
  if (value) {
    return true;
  }

  return error;
};
