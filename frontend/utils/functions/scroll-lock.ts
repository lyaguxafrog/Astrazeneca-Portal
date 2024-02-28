// https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight#Problems_and_solutions
const isTargetElementTotallyScrolled = (targetElement: any): boolean =>
  targetElement
    ? targetElement.scrollHeight - targetElement.scrollTop <= targetElement.clientHeight
    : false;

const preventDefault = (rawEvent: TouchEvent): boolean => {
  const e = rawEvent;

  // Do not prevent if the event has more than one touch (usually meaning this is a multi touch gesture like pinch to zoom)
  if (e.touches && e.touches.length > 1) {
    return true;
  }

  if (e.preventDefault) {
    e.preventDefault();
  }

  return false;
};

let initialClientY = -1;

const handleScroll = (event: TouchEvent, targetElement: any): boolean => {
  const clientY = event.targetTouches[0].clientY - initialClientY;

  if (targetElement && targetElement.scrollTop === 0 && clientY > 0) {
    // element is at the top of its scroll
    return preventDefault(event);
  }

  if (isTargetElementTotallyScrolled(targetElement) && clientY < 0) {
    // element is at the top of its scroll
    return preventDefault(event);
  }

  event.stopPropagation();
  return true;
};

let disabledCount = 0;

export function disableScroll(
  targetElement: HTMLElement | undefined = undefined,
  isMobile?: boolean
) {
  disabledCount++;
  document.documentElement.style.overflow = 'hidden';

  // TODO: обработать скролл двумя пальцами

  if (isMobile && targetElement) {
    targetElement.addEventListener('touchstart', (event: TouchEvent) => {
      if (event.targetTouches.length === 1) {
        // detect single touch
        initialClientY = event.targetTouches[0].clientY;
      }
    });

    targetElement.addEventListener('touchmove', (event: TouchEvent) => {
      if (event.targetTouches.length === 1) {
        // detect single touch
        handleScroll(event, targetElement);
      }
    });

    document.body.addEventListener('touchmove', preventDefault, { passive: false });
  }
}

export function enableScroll(
  targetElement: HTMLElement | undefined = undefined,
  isMobile?: boolean
) {
  if (disabledCount <= 0) {
    disabledCount = 0;
  } else {
    disabledCount--;
  }
  console.log(disabledCount);
  if (disabledCount !== 0) {
    return;
  }

  document.documentElement.style.overflow = 'initial';

  if (isMobile && targetElement) {
    targetElement.ontouchstart = null;
    targetElement.ontouchmove = null;

    document.body.removeEventListener('touchmove', preventDefault);
  }
}
