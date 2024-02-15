export type Project = {
  title: string;
  techs: string[];
  link: string;
  isComingSoon?: boolean;
};

const projects: Project[] = [
  {
    title: "NestJS Fastify Http Proxy",
    techs: ["NestJS"],
    link: "/",
    isComingSoon: true,
  },
  {
    title: "Obsidian Canvas Diff Plugin",
    techs: ["JS"],
    link: "/",
    isComingSoon: true,
  },
];

export default projects;
