type Social = {
  label: string;
  link: string;
};

type Presentation = {
  mail: string;
  title: string;
  description: string;
  socials: Social[];
  profile?: string;
};

const presentation: Presentation = {
  mail: "regulardev.click@gmail.com",
  title: "Hi, I’m Alexander 👋",
  // profile: "/profile.webp",
  description:
    "Hi, i'm a *frontend developer* with *4 years* of web experience. I am currently working with *NestJS, React and Typescript*.",
  socials: [
    {
      label: "Github",
      link: "https://github.com/alnikmakh",
    },
  ],
};

export default presentation;
