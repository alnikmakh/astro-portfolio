import type { TailwindColor } from "@/utils/types/tailwind";

type Theme = {
  colors: {
    primary: TailwindColor;
  };
};

const theme: Theme = {
  colors: {
    primary: "orange",
  },
};

export default theme;
