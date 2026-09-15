# Deploying

Remote: `https://github.com/benbishop/Portfolio-Site`
Pages URL for that repo name: `https://benbishop.github.io/Portfolio-Site/`

## Fix the history first

Two internal Skyllful diagrams, `feature-idea-map-web.jpg` and
`platform-functions-map-web.jpg`, were committed and pushed. The page does not use them.
They were meant to be excluded, but `.gitignore` ended up in the parent folder rather than
inside the repository, so it never applied.

Deleting them in a new commit is not enough. Both blobs stay reachable in the earlier
commit, and on a public repository anyone can pull them out of history. Since this is only
two commits and nobody else has cloned it, replacing the history outright is clean and
safe.

The files are already out of the working tree (moved to `_local-only/` in the parent
folder), and `.gitignore` and `.nojekyll` are now inside the repository. Run this in
Terminal:

    cd "/Users/benjaminbishop/Projects/Past Project Portfolio/Portfolio-Site/Portfolio Site"

    git checkout --orphan clean
    git add -A
    git commit -m "Portfolio: five case studies

    Talkthrough, seven years of design-to-code tooling, Click Catcher to
    heatmaps, NOV Remote, and the Data Review Tool.

    One page, no build step, no dependencies, no JavaScript."

    git branch -D main
    git branch -m main
    git push -f origin main

Then confirm:

    git log --oneline          # one commit
    git ls-files               # ten files, no *-map-web.jpg

On GitHub, check the Commits tab shows a single commit, and that
`public/work/feature-idea-map-web.jpg` 404s.

If anything goes wrong, the simpler alternative for a repository this new is to delete it
in **Settings, Danger Zone, Delete this repository**, create it again, and push. Nothing
is lost: no stars, no issues, no forks.

## Check the visibility

If the repository is public, the history fix above is urgent, because the two images are
reachable right now. If it is private, it is still worth doing before you make it public.

**Settings** shows the current state at the bottom of the General tab.

## The repository name costs you the good URL

Named `Portfolio-Site`, the site serves at `benbishop.github.io/Portfolio-Site/`.

GitHub serves a repository named exactly `<username>.github.io` at the bare account URL
instead. Renaming this repository to `benbishop.github.io` in **Settings, General** moves
the site to `https://benbishop.github.io`, which is the version you want on a resume and
the one a custom domain points at later. GitHub redirects the old remote automatically, so
an existing clone keeps working, though it is worth updating the remote anyway:

    git remote set-url origin https://github.com/benbishop/benbishop.github.io.git

You get one user site per account, so this is the repository to spend it on.

## Turn on Pages

**Settings, then Pages**:

- **Source:** Deploy from a branch
- **Branch:** `main`, folder `/ (root)`

First build takes a minute or two; later pushes go live in under a minute. Pages on a
private repository requires a paid plan. On a free account the repository has to be public
for the site to serve.

`.nojekyll` tells Pages to serve the files as they are instead of running them through
Jekyll. Nothing here needs Jekyll, and without that file any future folder starting with an
underscore would be dropped silently.

## Updating later

    git add -A
    git commit -m "what changed"
    git push

## The nesting

The repository currently sits at `Portfolio-Site/Portfolio Site/`, one folder inside
another with a near-identical name. It works, but the inner folder name contains a space,
which means quoting paths forever, and the duplication is easy to trip over later. Worth
flattening at some point. Not urgent, and not worth doing mid-fix.

## A custom domain, when you want one

1. Rename the repository to `benbishop.github.io` first, per above.
2. At your DNS provider, four A records for the apex pointing at `185.199.108.153`,
   `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, and a CNAME for `www`
   pointing at `benbishop.github.io`. Verify those addresses against GitHub's current
   documentation; they have changed before.
3. Enter the domain in **Settings, then Pages**. GitHub writes a `CNAME` file into the
   repository, so pull afterward.
4. Wait for the certificate, then tick **Enforce HTTPS**.

## Still open

`Portfolio-Catalog/TIME-SENSITIVE.md` item 3: confirming in writing what the separation
agreement permits you to show publicly. This page carries Skyllful Studio screenshots, the
annotated Lesson Builder working file, the Talkthrough prototype, named customers, and
internal feature names. Worth closing before the URL is indexed.
