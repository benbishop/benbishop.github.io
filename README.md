# benbishop.github.io

Benjamin Bishop, portfolio. One page, no build step, no dependencies, no JavaScript.

## Structure

    index.html      the page: markup and CSS in one file
    public/work/    images
    build.py        optional, inlines images into a single self-contained file
    .nojekyll       tells GitHub Pages to serve the files as-is

## Editing

Open `index.html`. The CSS lives in a `<style>` block at the top; color, type and
layout are all CSS custom properties on `:root`, redefined for dark mode.

The layout is one repeated structure:

    <section>
      <div class="row">
        <p class="tag">label in the left rail</p>
        <div class="body">prose, capped at a readable measure</div>
      </div>
    </section>

Use `class="body wide"` instead of `class="body"` where something should run the
full width: figures, tables, the image grid.

To add a case study, copy a `<section>` and its neighbours, then add a line to the
`<nav class="contents">` list near the top.

## Single-file version

    python3 build.py

Writes `index-standalone.html` with every image inlined as a data URI. Only needed
for sending the portfolio as one file. Deploying this folder does not use it.
