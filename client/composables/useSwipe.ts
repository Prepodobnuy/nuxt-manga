import { ref } from "vue";

interface SwipeDistance {
  x: number;
  y: number;
  stamp: number;
}

interface Params {
  minStamp?: number;
  length?: number;
}

export const useSwipe = () => {
  const handleSwipe = (
    start: SwipeDistance,
    end: SwipeDistance,
    params: Params | undefined,
  ) => {
    const maxStamp: number = params?.minStamp || 230;
    const length: number = params?.length || 170;

    const xLambda = end.x - start.x;
    const yLambda = end.y - start.y;
    const stampLambda = end.stamp - start.stamp;

    if (stampLambda > maxStamp) return { left: false, right: false };

    const left = xLambda > length;
    const right = xLambda < -length;

    return {
      left: left,
      right: right,
    };
  };

  return {
    handleSwipe,
  };
};
