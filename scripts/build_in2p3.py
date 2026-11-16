"""Build IN2P3_2026.html: a 15-min cut of LBNL2026.html for the IN2P3/IRFU ML workshop."""
import re
import sys

src_path, paris_path, out_path = sys.argv[1:4]
src = open(src_path, encoding="utf-8").read()
paris = open(paris_path, encoding="utf-8").read()


def extract(html, sid):
    """Return the full <section id=sid ...>...</section> block, respecting nesting."""
    m = re.search(r'<section[^>]*\bid="%s"' % re.escape(sid), html)
    if not m:
        raise KeyError(sid)
    start = m.start()
    depth = 0
    for t in re.finditer(r'<section\b|</section>', html[start:]):
        depth += 1 if t.group(0) == '<section' else -1
        if depth == 0:
            return html[start:start + t.end()]
    raise ValueError(sid)


# ---- head / tail -------------------------------------------------------------
slides_open = src.index('<div class="slides">') + len('<div class="slides">')
head = src[:slides_open]
last = extract(src, "work-with-us")
tail = src[src.index(last) + len(last):]
head = re.sub(r'<title>.*?</title>',
              '<title>Lightcone Research &mdash; IN2P3/IRFU Machine Learning Workshop 2026</title>', head)

# ---- title slide -------------------------------------------------------------
title = '''<section id="title" data-background-color="var(--lc-bg)">

        <span class="masthead-rule" aria-hidden="true"></span>

        <div style="position: absolute; left: 56pt; right: 56pt; top: 38%; transform: translateY(-50%); display: flex; flex-direction: column; align-items: center;">

          <p style="font-family: var(--lc-font-ui); font-size: 11pt; font-weight: 600; letter-spacing: 0.24em; text-transform: uppercase; color: var(--lc-primary); margin: 0 0 14pt 0;">Lightcone Research</p>

          <div class="title-display" style="font-size: 31pt; max-width: 1000px; text-align: center; margin: 0;">
            An open ecosystem for reproducible, composable<br>and verifiable physics analyses<br>in the age of AI&nbsp;agents
          </div>

          <hr style="width: 80px; margin: 24pt auto 20pt;">

          <p style="font-family: var(--lc-font-ui); margin: 0; text-align: center; line-height: 1.5; max-width: 860px;">
            <span style="display: block; font-size: 13.5pt; font-weight: 600; color: var(--lc-primary); letter-spacing: 0.01em;">IN2P3/IRFU Machine Learning Workshop 2026</span>
            <span style="display: block; margin-top: 5pt; font-size: 12pt; color: var(--lc-muted);">LPSC Amphitheatre, Grenoble &amp; Zoom &middot; Tuesday 17 November 2026</span>
          </p>

        </div>

        <div style="position: absolute; left: 56pt; bottom: 92pt; display: flex; align-items: center; gap: 13pt;">
          <img src="assets/team/alex.png" alt="Alexandre"
               style="width: 62pt; height: 62pt; border-radius: 50%; object-fit: cover; box-shadow: 0 0 0 2pt var(--lc-bg), 0 0 0 3pt var(--lc-warm), 0 2pt 6pt rgba(0,0,0,0.12);">
          <div style="text-align: left;">
            <p style="font-size: 15pt; color: var(--lc-text); margin: 0; font-weight: 600; line-height: 1.2;">Alexandre Boucaud</p>
            <p style="font-size: 10.5pt; color: var(--lc-muted); margin: 4pt 0 0 0; line-height: 1.25;">CNRS &middot; APC / IN2P3</p>
            <p style="font-size: 10.5pt; color: var(--lc-muted); margin: 3pt 0 0 0; line-height: 1.25;">Technical lead, Lightcone Research</p>
          </div>
        </div>

        <div style="position: absolute; right: 56pt; bottom: 96pt; display: flex; align-items: center; gap: 30pt;">
          <img src="assets/aissai.png" alt="AISSAI &mdash; CNRS" style="height: 42pt; width: auto; object-fit: contain; position: relative; top: 6pt;">
          <img src="assets/bids_logo.png" alt="Berkeley Institute for Data Science" style="height: 46pt; width: auto; object-fit: contain;">
        </div>
      </section>'''

# ---- substrate: cite the position paper (its own slide is cut) -----------------
substrate = extract(src, "position-substrate")
cite = '''
        <p style="position: absolute; left: 0; right: 0; bottom: -6pt; text-align: center; font-size: 9pt; color: var(--lc-muted); margin: 0;">
          Lanusse &amp; Parker (2026), <em>Science that Compounds: the Need for a New Substrate for Research in the Age of AI</em>
        </p>
      </section>'''
substrate = substrate[:substrate.rindex('</section>')] + cite.strip()

# ---- Hubble slide: fold in the DESI case title -------------------------------
hubble = extract(src, "result-hubble").replace(
    '            Hubble diagram\n',
    '            First pilot &middot; DESI DR1 BAO <span style="color: var(--lc-muted); font-size: 18pt;">(arXiv:2404.03000)</span> &mdash; Hubble diagram reproduced\n')
assert 'First pilot' in hubble

# ---- IN2P3 slide (adapted from Paris2026 #needs) -----------------------------
_ = extract(paris, "needs")  # source of the layout; text rewritten in English below


def card(idx, color, icon, heading, body, tag=None):
    tag_html = ('<span style="font-family: var(--lc-font-ui); font-size: 8pt; font-weight: 600; letter-spacing: 0.14em; '
                'text-transform: uppercase; color: var(--lc-%s); border: 1px solid var(--lc-%s); border-radius: 3pt; '
                'padding: 1pt 5pt; margin-left: 8pt; vertical-align: 2pt;">%s</span>' % (color, color, tag)) if tag else ''
    return f'''
            <div class="fragment fade-up card-glow" data-fragment-index="{idx}" style="padding: 11pt 14pt; border-left: 3px solid var(--lc-{color});">
              <p style="font-size: 12.5pt; margin: 0 0 4pt 0; font-family: var(--lc-font-heading); color: var(--lc-{color}); font-weight: 600;">
                <i class="fa-solid {icon}" style="margin-right: 6pt;"></i>{heading}{tag_html}
              </p>
              <p style="font-size: 10.5pt; line-height: 1.45; margin: 0; color: var(--lc-muted);">
                {body}
              </p>
            </div>'''


def group(color, icon, label, top):
    return f'''
          <div style="display: flex; align-items: center; gap: 10pt; margin: {top}pt 0 10pt 0;">
            <p style="font-family: var(--lc-font-ui); font-size: 11pt; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--lc-{color}); margin: 0;">
              <i class="fa-solid {icon}" style="margin-right: 6pt;"></i>{label}
            </p>
            <span style="flex: 1; height: 1px; background: rgba(var(--lc-{color}-rgb), 0.25);"></span>
          </div>'''


in2p3 = f'''<section id="in2p3" data-background-glow>
        <span class="section-label">Lightcone at IN2P3</span>
        <h2 style="font-size: 24pt; margin-bottom: 12pt;">Bringing the stack to our computing centres</h2>
        <div style="display: flex; flex-direction: column;">
{group("primary", "fa-server", "What we are deploying", 0)}
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10pt;">
{card(0, "primary", "fa-microchip", "CC-IN2P3",
      'Inventory of the Lightcone components that can be installed at the centre, and the <strong style="color: var(--lc-text);">SLURM pilot-job backend</strong> so that <code>lc materialize</code> runs there unchanged.', "in progress")}
{card(1, "secondary", "fa-cloud", "VirtualData &middot; Paris-Saclay",
      'Kubernetes, <strong style="color: var(--lc-text);">Dask Gateway</strong> and JupyterHub as an interactive backend behind the same execution interface.', "exploring")}
          </div>
{group("warm", "fa-list-check", "What we need", 16)}
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10pt;">
{card(2, "warm", "fa-key", "Agent-ready HPC access",
      'Today&rsquo;s security and access models do not let agentic workflows use HPC resources to their full capacity.')}
{card(3, "accent", "fa-graduation-cap", "Shared best practices",
      'A coordinated effort to collect and spread good practice with generative AI &mdash; from PhD training to the research workflow.')}
{card(4, "highlight", "fa-bolt", "Inference for everyone",
      'Shared, secure access to frontier models for individuals and projects. <strong style="color: var(--lc-text);">More in my lightning talk at 10:20.</strong>')}
          </div>
        </div>
      </section>'''

# ---- Fellowship slide ----------------------------------------------------------
fellowship = '''<section id="fellowship" data-background-glow>
        <div style="display: grid; grid-template-columns: 1fr 250pt; gap: 34pt; align-items: center; height: 100%;">

          <div>
            <p style="font-family: var(--lc-font-ui); font-size: 10pt; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; color: var(--lc-muted); margin: 0 0 10pt 0;">
              <i class="fa-solid fa-flask" style="margin-right: 6pt; color: var(--lc-warm);"></i>The next pilot is your science
            </p>
            <div class="hero-title" style="font-size: 34pt; letter-spacing: -0.015em; line-height: 1.1; margin: 0 0 10pt 0; color: var(--lc-text);">
              Become a Lightcone Research Fellow
            </div>
            <p style="font-family: var(--lc-font-heading); font-size: 15pt; font-style: italic; color: var(--lc-warm); line-height: 1.35; margin: 0 0 16pt 0;">
              A three-month remote fellowship: apply AI agents to your own research project, and help shape the tools.
            </p>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12pt;">
              <div class="card-glow" style="padding: 11pt 14pt; border-left: 3px solid var(--lc-primary);">
                <p style="font-family: var(--lc-font-ui); font-size: 8.5pt; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: var(--lc-primary); margin: 0 0 6pt 0;">
                  <i class="fa-solid fa-gift" style="margin-right: 5pt;"></i>You get
                </p>
                <ul style="font-size: 10.5pt; line-height: 1.45; margin: 0; padding-left: 14pt; color: var(--lc-muted);">
                  <li>Individual onboarding, direct Slack access to the team</li>
                  <li>Claude / Codex credits</li>
                  <li>A weekly call with a small cross-disciplinary cohort (4&ndash;6 Fellows)</li>
                  <li>A talk at the <strong style="color: var(--lc-text);">Paris Agentic AI for Science Summit</strong> (end Feb. 2027), with travel support</li>
                </ul>
              </div>
              <div class="card-glow" style="padding: 11pt 14pt; border-left: 3px solid var(--lc-accent);">
                <p style="font-family: var(--lc-font-ui); font-size: 8.5pt; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: var(--lc-accent); margin: 0 0 6pt 0;">
                  <i class="fa-solid fa-user-astronaut" style="margin-right: 5pt;"></i>You bring
                </p>
                <ul style="font-size: 10.5pt; line-height: 1.45; margin: 0; padding-left: 14pt; color: var(--lc-muted);">
                  <li>Early-career researcher, any discipline</li>
                  <li>A concrete project aimed at publication by spring 2027 &mdash; ongoing or nearly done is welcome</li>
                  <li>Your own compute: laptop, lab cluster or HPC (CC-IN2P3, NERSC&hellip;)</li>
                  <li>Your PI&rsquo;s agreement</li>
                </ul>
              </div>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <img src="assets/qr-fellowship.svg" alt="QR code to lightconeresearch.org/fellowship"
                 style="width: 200pt; height: 200pt; background: #fff; padding: 8pt; border-radius: 6pt; box-shadow: 0 6pt 18pt rgba(0,0,0,0.12);">
            <p style="font-family: var(--lc-font-heading); font-size: 20pt; color: var(--lc-warm); margin: 14pt 0 2pt 0; font-weight: 600;">Apply by Friday 20&nbsp;Nov</p>
            <p style="font-family: var(--lc-font-ui); font-size: 11pt; margin: 0;">
              <a href="https://www.lightconeresearch.org/fellowship" target="_blank" style="color: var(--lc-secondary); text-decoration: none;">lightconeresearch.org/fellowship</a>
            </p>
          </div>
        </div>

        <p style="position: absolute; left: 0; right: 0; bottom: -4pt; text-align: center; font-family: var(--lc-font-ui); font-size: 10pt; color: var(--lc-muted); margin: 0; letter-spacing: 0.03em;">
          <i class="fa-brands fa-github" style="color: var(--lc-primary); margin-right: 5pt;"></i>ASTRA is developed in the open, by RFC &mdash; <a href="https://astra-spec.org" style="color: var(--lc-text); text-decoration: none;">astra&#8209;spec.org</a>
          &nbsp;&middot;&nbsp;
          <i class="fa-solid fa-envelope" style="color: var(--lc-primary); margin-right: 5pt;"></i><a href="mailto:info@lightconeresearch.org" style="color: var(--lc-text); text-decoration: none;">info@lightconeresearch.org</a>
          &nbsp;&middot;&nbsp;
          <i class="fa-brands fa-discord" style="color: var(--lc-primary); margin-right: 5pt;"></i><a href="https://discord.gg/EbG6JKuyAx" style="color: var(--lc-text); text-decoration: none;">Discord</a>
        </p>
      </section>'''

backup_divider = '''<section id="backup" data-background-glow>
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
          <div class="hero-title" style="font-size: 54pt; letter-spacing: -0.02em; margin: 0 0 10pt 0;">Backup</div>
          <p style="font-size: 14pt; color: var(--lc-muted); margin: 0;">ASTRA schema details &middot; agent skills &middot; team &amp; hiring</p>
        </div>
      </section>'''

main = [title,
        extract(src, "accel"), extract(src, "trajectory"), extract(src, "pressure"),
        extract(src, "the-question"), substrate,
        extract(src, "overview"), extract(src, "stack"),
        extract(src, "astra-schema"), extract(src, "astra-universes"),
        extract(src, "lc-cli-demo"), extract(src, "lc-cli-engine"), extract(src, "lc-cli-venues"),
        hubble, extract(src, "result-dag"),
        in2p3, fellowship]
backup = [backup_divider, extract(src, "astra-elements"), extract(src, "astra-insights"),
          extract(src, "lc-cli-skills"), extract(src, "hiring"), extract(src, "work-with-us")]

sep = "\n\n      "
body = "\n      " + sep.join(main) + sep + "<!-- ======================= BACKUP ======================= -->" + sep + sep.join(backup) + "\n"
open(out_path, "w", encoding="utf-8").write(head + body + tail)
print("main slides:", len(main), "backup:", len(backup))
