export const required = (
  value: string | number | unknown[] | null,
  error = 'Поле обязательно для заполенения'
) => {
  if (Array.isArray(value)) {
    return !value.length ? error : true;
  }

  if (value) {
    return true;
  }

  return error;
};
