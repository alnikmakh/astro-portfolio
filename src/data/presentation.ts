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
  profile: "/profile.webp",
  description:
    "I'm a *Senior Full Stack JavaScript Developer* with *6 years* of web experience. I am currently working with *JavaScript , TypeScript, React, Next.js, Vue.js, Node.js, NestJS, GraphQL, PostgreSQL, Redis, Kafka, and Docker*.",
  socials: [
    {
      label: "Github",
      link: "https://github.com/alnikmakh",
    },
  ],
};

export default presentation;
