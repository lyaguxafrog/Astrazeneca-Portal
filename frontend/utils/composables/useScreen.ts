export const BREAKPOINTS = {
  smallMobile: 359,
  mobile: 560,
  tablet: 768,
  laptop: 992,
  desktop: 1200,
};

export function useScreen() {
  const $device = useDevice();

  const screen = useState('screen', () => ({
    windowWidth: 0,
  }));

  const initBreakpoints = () => {
    if (process.client) {
      screen.value.windowWidth = window.innerWidth;

      window.addEventListener('resize', () => {
        screen.value.windowWidth = window.innerWidth;
      });
    }
  };

  const breakpoints = computed(() => {
    if (process.client) {
      const windowWidth = screen.value.windowWidth;
      return {
        xs: windowWidth < BREAKPOINTS.mobile,
        sm: windowWidth >= BREAKPOINTS.mobile && windowWidth < BREAKPOINTS.tablet,
        smAndDown: windowWidth < BREAKPOINTS.tablet,
        md: windowWidth >= BREAKPOINTS.tablet && windowWidth < BREAKPOINTS.laptop,
        mdAndDown: windowWidth < BREAKPOINTS.laptop,
        lg: windowWidth >= BREAKPOINTS.laptop && windowWidth < BREAKPOINTS.desktop,
        lgAndDown: windowWidth < BREAKPOINTS.desktop,
        xl: windowWidth >= BREAKPOINTS.desktop,
      };
    } else {
      return {
        xs: $device.isMobile,
        sm: $device.isMobile,
        smAndDown: $device.isMobileOrTablet,
        md: $device.isMobileOrTablet,
        mdAndDown: $device.isMobileOrTablet,
        lg: $device.isDesktop,
        lgAndDown: $device.isDesktop,
        xl: $device.isDesktop,
      };
    }
  });

  return {
    initBreakpoints,
    $screen: readonly(breakpoints),
  };
}
