export type Loadable<T> = {
  data: T | undefined;
  loaded: boolean;
};

export const loadableEmpty = <T>(defaultData?: T): Loadable<T> => ({
  data: defaultData,
  loaded: false,
});
