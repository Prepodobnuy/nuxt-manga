import type { Ref } from "vue";

interface TouchState {
  startX: number;
  startY: number;
  startTime: number;
  isLongPress: boolean;
}

interface GestureCallbacks {
  onSwipeLeft: (index: number) => void;
  onSwipeRight: (index: number) => void;
  onSwipeUp: (index: number) => void;
  onSwipeDown: (index: number) => void;
}

export function useTouchGestures(callbacks: GestureCallbacks) {
  const touchStates = new Map<number, TouchState>();
  const LONG_PRESS_DURATION = 100;

  const handleTouchStart = (index: number, event: TouchEvent) => {
    const touch = event.touches[0];
    touchStates.set(index, {
      startX: touch.clientX,
      startY: touch.clientY,
      startTime: Date.now(),
      isLongPress: false,
    });

    const timer = setTimeout(() => {
      const state = touchStates.get(index);
      if (state) {
        state.isLongPress = true;
      }
    }, LONG_PRESS_DURATION);

    // Очистка таймера при перемещении или отпускании
    const cleanup = () => {
      clearTimeout(timer);
      window.removeEventListener("touchend", cleanup);
      window.removeEventListener("touchmove", cleanup);
    };

    window.addEventListener("touchend", cleanup, { once: true });
    window.addEventListener("touchmove", cleanup, { once: true });
  };

  const handleTouchMove = (index: number, event: TouchEvent) => {
    event.preventDefault(); // Предотвращаем скролл страницы
  };

  const handleTouchEnd = (index: number) => {
    const state = touchStates.get(index);
    if (!state) return;

    const { startX, startY, startTime, isLongPress } = state;
    const deltaTime = Date.now() - startTime;
    const touch = event.changedTouches[0];
    const deltaX = touch.clientX - startX;
    const deltaY = touch.clientY - startY;

    if (isLongPress && deltaTime >= LONG_PRESS_DURATION) {
      const absDeltaX = Math.abs(deltaX);
      const absDeltaY = Math.abs(deltaY);

      if (absDeltaX > absDeltaY) {
        // Горизонтальный свайп
        if (deltaX > 0) {
          callbacks.onSwipeRight(index);
        } else {
          callbacks.onSwipeLeft(index);
        }
      } else {
        // Вертикальный свайп
        if (deltaY > 0) {
          callbacks.onSwipeDown(index);
        } else {
          callbacks.onSwipeUp(index);
        }
      }
    }

    touchStates.delete(index);
  };

  return {
    handleTouchStart,
    handleTouchMove,
    handleTouchEnd,
  };
}
