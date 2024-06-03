export const generatePathFromTitleAndSlug = (title: string, slug: string) => {
    const pathFromTitle = title
        .toLowerCase()                                        // Convert to lowercase
        .replace(/[^a-z0-9\s]/g, '')    // Remove special characters
        .replace(/\s+/g, '-')           // Replace spaces with hyphens
        .trim();                                               // Remove any leading or trailing spaces


    return `${slug.split('-')[0]}-${pathFromTitle}`;
}
