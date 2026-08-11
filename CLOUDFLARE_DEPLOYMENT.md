# Deploy the Tennessee Lunabotics wiki with MkDocs on Cloudflare Pages

These files are intended to be added to the existing public repository:
`TennesseeLunabotics/wiki`.

## 1. Add the migration files

Copy these files into the repository root:

- `mkdocs.yml`
- `requirements.txt`
- `prepare_docs.py`

Add the two lines from `.gitignore.additions` to the repository's `.gitignore`.
The original GitBook Markdown and `.gitbook/assets` stay in place; the converter
builds a temporary `docs/` tree for MkDocs.

## 2. Test locally

From the repository root:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python prepare_docs.py
mkdocs serve
```

Open the local URL printed by MkDocs. Before deploying, click through image-heavy
pages and the Client/Server sections to verify the GitBook HTML renders as expected.

For a production-style local build:

```bash
python prepare_docs.py
mkdocs build
```

The static site is written to `site/`.

## 3. Commit and push

```bash
git add mkdocs.yml requirements.txt prepare_docs.py .gitignore
git commit -m "Migrate wiki from GitBook to MkDocs"
git push
```

## 4. Create the Cloudflare Pages project

In Cloudflare Dashboard:

1. Go to **Workers & Pages**.
2. Choose **Create application** → **Pages** → **Connect to Git**.
3. Select `TennesseeLunabotics/wiki`.
4. Use the repository's production branch (currently `master`).
5. Set the build command to:

   ```bash
   python -m pip install -r requirements.txt && python prepare_docs.py && mkdocs build
   ```

6. Set **Build output directory** to:

   ```text
   site
   ```

7. Leave the root directory at the repository root.
8. Save and deploy.

This produces a `*.pages.dev` URL first. Verify that URL before changing DNS.

## 5. Attach `wiki.tennesseelunabotics.com`

Do this from the **Pages project**, not by manually pointing an A record at a
Cloudflare IP:

1. In the Pages project, open **Custom domains**.
2. Add `wiki.tennesseelunabotics.com`.
3. Cloudflare will create/guide the appropriate DNS record for the Pages project.
4. Remove the old `wiki` A record that points to `172.67.187.182`.

The old A record is the record that caused Cloudflare Error 1000 ("DNS points to
prohibited IP"). A Pages custom domain should be associated with the Pages project,
not pinned to a Cloudflare anycast IP.

## 6. Future editing workflow

Continue editing the existing Markdown files in the repository root,
`systems-engineering/`, and `programming/`. Do **not** edit generated `docs/`.
Every Cloudflare build runs `prepare_docs.py`, regenerates the MkDocs source, and
publishes the result.

To add a new page, also add it to the `nav:` section in `mkdocs.yml`.

## Optional: Doxygen later

Keep MkDocs as the human-authored knowledgebase. If the robot software repository
needs API/class documentation, generate Doxygen separately and either link to it
from MkDocs or copy Doxygen's HTML output under a dedicated static path during the
build. That avoids mixing generated code reference pages with the team's curated
engineering documentation.
