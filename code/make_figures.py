# Academic Figure Skill Asset Confirmation (verified against assets/figures/)
# (a) heatmap, finest unit x tumour type   -> cross-type inherit (heatmap/CorrHeatmap colormap)  -> param inherit
# (b) horizontal bar, risk evaluation unit -> cross-type inherit (BarCategorical)               -> param inherit
# (c) bar, share with size stratification  -> cross-type inherit (BarCategorical)               -> param inherit
# Fig 1 (PRISMA-ScR flow)                  -> no matching asset (schematic)                     -> param inherit
# NOTE: the skill's compose_figure() grid was tried first; its default spacing made panels b/c collide at 183 mm,
#       so Fig 2 uses an explicit GridSpec (hero panel a spans both rows, 1.35:1 width ratio, as in the skill's hero layout).
# RULE: Rscript is not installed on this machine, so no R production script was run (Python only).
"""Figures for the scoping review (Academic Figure Skill conventions):
  Fig. 1 PRISMA-ScR flow diagram; graphical abstract; Fig. 2 three-panel figure
  (finest unit x tumour type heatmap, unit at which risk estimation is evaluated, size stratification by tumour type).
Counts come from supplement/S5_extraction_table.tsv; the flow-diagram numbers are written into fig_prisma().
Run from the repository root:  python3 code/make_figures.py   Output: figures/*.pdf and *.png"""
import collections, os, sys

# Academic Figure Skill Typography Baseline — COPY VERBATIM, place at TOP of script
import matplotlib as mpl
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans"],
    "font.size": 8,
    "axes.titlesize": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 8,
    "figure.titlesize": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "legend.frameon": False,
})

# Academic Figure Skill Nature/Cell/Science Color Palette -- COPY VERBATIM
CATEGORICAL = ["#2166AC", "#B2182B", "#1B7837", "#F1A340", "#762A83", "#666666"]
CATEGORICAL_EXTENDED = [
    "#2166AC", "#B2182B", "#1B7837", "#F1A340", "#762A83", "#666666",
    "#4393C3", "#D6604D", "#5AAE61", "#B35806", "#9970AB", "#999999",
]
DIVERGING   = ["#2166AC", "#F7F7F7", "#B2182B"]
SEQUENTIAL  = ["#F7FBFF", "#6BAED6", "#08306B"]
ACCENT_RED  = "#B2182B"
GREY        = "#999999"
BLACK       = "#222222"

# Academic Figure Skill Export Baseline — COPY VERBATIM
mpl.rcParams.update({
    "pdf.fonttype": 42,         # TrueType font embedding
    "svg.fonttype": "none",     # editable text in SVG
    "savefig.bbox": "tight",    # trim whitespace
    "savefig.dpi": 300,
})

def save_cns_figure(fig, filename):
    """Standard Academic Figure Skill export: vector PDF + 300dpi PNG preview."""
    fig.savefig(f"{filename}.pdf", bbox_inches="tight", dpi=300)
    fig.savefig(f"{filename}.png", bbox_inches="tight", dpi=300)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(D, 'figures')
import csv
import matplotlib.gridspec as gridspec

# ---------------- data (all rows used; nothing dropped or sampled) ----------------
with open(os.path.join(D, 'supplement', 'S5_extraction_table.tsv'), encoding='utf-8', newline='') as f:
    inc = list(csv.DictReader(f, delimiter='\t'))          # the 330 included papers
FINEST, TUMOUR = 'Finest evaluation unit', 'Tumour type'
rev = [r for r in inc if r[FINEST] == 'Review (no own results)' or r['Paper type'] == 'Review']
non = [r for r in inc if r not in rev]
full = [r for r in non if r['Evidence basis'] == 'Full text']
TUM = [('Glioma', 'Glioma'), ('Brain metastasis', 'Brain metastasis'), ('Meningioma', 'Meningioma'),
       ('Paediatric', 'Paediatric'), ('Multiple types', 'Multiple types'), ('Unknown', 'Unspecified')]
UNI = [(u, u) for u in ('Voxel', 'Image', 'Patient', 'Lesion')]
M = np.array([[sum(1 for r in full if r[TUMOUR] == t and r[FINEST] == u) for u, _ in UNI] for t, _ in TUM], float)
unit_unknown = len(full) - int(M.sum())

rk = [r for r in non if r['Risk evaluation unit'] != '']      # papers with a risk-estimation method
rc = collections.Counter(None if r['Risk evaluation unit'] == 'Not stated' else r['Risk evaluation unit'] for r in rk)
risk_items = sorted(((k, v) for k, v in rc.items() if k), key=lambda kv: -kv[1])
risk_unstated = rc.get(None, 0)
size_rows = [(t_en, sum(r['Stratified by lesion size'].startswith('Yes') for r in non if r[TUMOUR] == t), sum(1 for r in non if r[TUMOUR] == t)) for t, t_en in TUM]

# ---------------- Fig 2 panels ----------------
def panel_heat(ax, spec=None):
    cmap = LinearSegmentedColormap.from_list('seq', SEQUENTIAL)
    # row-normalised colour so every tumour type shows where its papers sit; counts are printed
    rows_n = M.sum(1, keepdims=True); rows_n[rows_n == 0] = 1
    P = M / rows_n
    im = ax.imshow(P, cmap=cmap, vmin=0, vmax=1, aspect='auto')
    cax = ax.inset_axes([0.28, -0.165, 0.44, 0.022])
    cb = ax.figure.colorbar(im, cax=cax, orientation='horizontal', ticks=[0, .5, 1])
    cb.ax.set_xticklabels(['0', '50', '100%']); cb.set_label('Share of tumour-type row', fontsize=6.5, labelpad=1)
    cb.ax.tick_params(labelsize=6, length=2, width=.5); cb.outline.set_linewidth(.4)
    ax.set_xticks(range(len(UNI))); ax.set_xticklabels([e for _, e in UNI])
    ax.set_yticks(range(len(TUM))); ax.set_yticklabels(['%s\n(n = %d)' % (e, M[i].sum()) for i, (_, e) in enumerate(TUM)])
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(j, i, int(M[i, j]), ha='center', va='center', fontsize=7,
                    color='white' if P[i, j] > .55 else BLACK)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    ax.set_xlabel('Finest evaluation unit reported', fontsize=7)
    ax.set_title('Finest unit, by tumour type\n(full text read; colour = row share)', fontsize=7.5, pad=14, loc='left')
    ax.xaxis.set_label_position('bottom')

def panel_risk(ax, spec=None):
    labs = [k.replace(' + ', '+') for k, _ in risk_items][::-1]
    vals = [v for _, v in risk_items][::-1]
    cols = [ACCENT_RED if k == 'Lesion' else CATEGORICAL[0] for k, _ in risk_items][::-1]
    ax.barh(labs, vals, color=cols, height=.7)
    for y, v in enumerate(vals): ax.text(v + 1, y, str(v), va='center', fontsize=7)
    ax.set_xlim(0, max(vals) * 1.15)
    ax.set_xlabel('Papers (n)', fontsize=7)
    ax.set_title('Unit at which risk estimation is evaluated\n(papers; n = %d, %d not stated)' % (sum(vals) + risk_unstated, risk_unstated), fontsize=7.5, loc='left', pad=14)

def panel_size(ax, spec=None):
    lab = [t for t, _, _ in size_rows][::-1]
    share = [100 * k / n if n else 0 for _, k, n in size_rows][::-1]
    ax.barh(lab, share, color=CATEGORICAL[0], height=.7)
    for y, (_, k, n) in enumerate(size_rows[::-1]): ax.text(share[y] + 1.5, y, '%d/%d' % (k, n), va='center', fontsize=7)
    ax.set_xlim(0, 100); ax.set_xlabel('Size-stratified results (% of papers)', fontsize=7)
    ax.set_title('Size stratification, by tumour type\n(all %d non-review papers)' % len(non), fontsize=7.5, loc='left', pad=14)

# ---------------- Fig 1: PRISMA-ScR flow ----------------
def box(ax, x, y, w, h, text, fc='#F7F7F7', ec='#444444'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=1.2', fc=fc, ec=ec, lw=0.6))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=6.5, linespacing=1.35, color=BLACK)
def arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='-|>', color='#444444', lw=0.6, mutation_scale=6))

def fig_prisma():
    mm = 1 / 25.4
    fig = plt.figure(figsize=(183 * mm, 176 * mm))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 183); ax.set_ylim(8, 180); ax.axis('off')
    BLUE, RED_L, GRN = '#E8F0F8', '#F6E6E8', '#E7F2E9'
    L, W, X2, W2 = 4, 94, 108, 71
    steps = [
        (150, 18, BLUE, 'Records identified\nPubMed / OpenAlex / arXiv 8,202;  Web of Science 3,119;\nScopus 4,972;  citation tracking 406 (new only)\nn = 16,699'),
        (122, 16, BLUE, 'Unique records after de-duplication\nn = 6,953'),
        (96, 16, BLUE, 'Title / abstract screening\n(AI screen + independent AI check)\nn = 6,953'),
        (66, 24, BLUE, 'Taken to full-text stage\nn = 343 (included 308 + unclear 35)\n+ 148 added by two blinded re-reviews (risk 98, metric 50)\n+ 12 from title-only E4 abstract re-screen'),
        (42, 14, BLUE, 'Full-text stage, data extracted\nn = 503'),
        (10, 24, GRN, 'Included  n = 330\nnon-review 313 (full text read 277, abstract only 36)\nreviews 17;  risk-estimation methods 160 (8 reviews)'),
    ]
    for y, h, fc, t in steps: box(ax, L, y, W, h, t, fc)
    side = [
        (128, 12, '#F7F7F7', 'Duplicates removed\nn = 9,746'),
        (90, 28, RED_L, 'Excluded  n = 6,535\nE4 voxel-only metrics 3,092;  E3 1,133;  E5 839;\nE1 546;  E7 408;  E6 253;  E2 168;  E8 90;\nE9 5;  other 1  (+4 non-brain reference records)'),
        (68, 14, RED_L, 'Unclear, not taken forward\nn = 71 (no abstract or full text)'),
        (30, 30, RED_L, 'Excluded  n = 171\nF0 full text not retrieved 35;  E4 92;  E5 15;\nE9 duplicates 10;  E7 8;  E3 4;  E1 3;  E2 1;\nother full-text reasons 2;  publication date 1\n(2 further records unresolved)'),
    ]
    for y, h, fc, t in side: box(ax, X2, y, W2, h, t, fc)
    cx = L + W / 2
    for (y1, y2) in [(150, 138), (122, 112), (96, 91), (66, 56), (42, 34)]: arrow(ax, cx, y1, cx, y2)
    for (y, yy) in [(134, 134), (104, 104), (75, 75), (45, 45)]: arrow(ax, L + W, y, X2, yy)
    ax.text(L, 178, 'PRISMA-ScR flow of study selection', fontsize=9, fontweight='bold', va='top')
    save_cns_figure(fig, os.path.join(OUT, 'fig1_PRISMA-ScR'))
    plt.close(fig)


# ---------------- Graphical abstract ----------------
def fig_graphical():
    from matplotlib.patches import Circle, Ellipse
    mm = 1 / 25.4
    fig = plt.figure(figsize=(183 * mm, 76 * mm))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 183); ax.set_ylim(4, 80); ax.axis('off')
    ax.text(3, 78.5, 'Missed lesions in brain tumour MRI segmentation: scoping review of %d papers' % len(inc),
            fontsize=9, fontweight='bold', va='top')
    xs = [3, 64, 125]; w = 55; top, bot = 70, 6
    heads = ['1  Voxel totals hide a missed lesion', '2  Lesion level is measured, but rarely', '3  Risk is not estimated per lesion']
    for x, h in zip(xs, heads):
        ax.add_patch(FancyBboxPatch((x, bot), w, top - bot, boxstyle='round,pad=0,rounding_size=1.5', fc='#FAFAFA', ec='#BBBBBB', lw=0.6))
        ax.text(x + 3, top - 2.5, h, fontsize=7, fontweight='bold', va='top', color=BLACK)
    PAD = 3.5
    # panel 1: schematic
    x0 = xs[0]
    ax.text(x0 + PAD, 58, 'Overlap scores over all voxels are\ndominated by large lesions.', fontsize=6.5, va='top', linespacing=1.3)
    ax.add_patch(Ellipse((x0 + 18, 38), 24, 18, fc='#F1A340', ec='none', alpha=.35))
    ax.add_patch(Ellipse((x0 + 18, 38), 21, 15, fc='none', ec=CATEGORICAL[0], lw=1.0))
    ax.add_patch(Circle((x0 + 42, 32), 3.2, fc='#F1A340', ec='none', alpha=.35))
    ax.add_patch(Circle((x0 + 42, 32), 3.2, fc='none', ec=ACCENT_RED, lw=1.0, ls=(0, (2, 1.5))))
    ax.text(x0 + 18, 24.5, 'large lesion: found', ha='center', fontsize=6.5, color=CATEGORICAL[0])
    ax.text(x0 + 42, 26.5, 'small lesion:\nmissed', ha='center', va='top', fontsize=6.5, color=ACCENT_RED, linespacing=1.2)
    ax.text(x0 + PAD, 11.5, 'Fill: reference lesion;  outline: prediction', fontsize=6.0, color='#555555', va='center')
    # panel 2: bars
    x0 = xs[1]
    ax.text(x0 + PAD, 58, 'Studies whose finest evaluation unit\nis the lesion', fontsize=6.5, va='top', linespacing=1.3)
    n_l = sum(1 for r in full if r[FINEST] == 'Lesion'); n_f = len(full)
    bars = [('Included studies, full text read (n = %d)' % n_f, 100 * n_l / n_f, '%d (%d%%)' % (n_l, round(100 * n_l / n_f))),
            ('Random PubMed sample (n = 60)', 100 * 3 / 60, '3 (5%)')]
    bmax = 33
    for i, (lab, v, txt) in enumerate(bars):
        y = 40 - i * 13
        ax.text(x0 + PAD, y + 3.5, lab, fontsize=6.0, va='bottom')
        ax.add_patch(plt.Rectangle((x0 + PAD, y - 2.5), bmax * v / 100, 5, fc=CATEGORICAL[0] if i == 0 else GREY, ec='none'))
        ax.text(x0 + PAD + bmax * v / 100 + 1.5, y, txt, fontsize=6.5, va='center')
    ax.text(x0 + PAD, 12, 'Size-stratified results: 84/313 papers\n(metastasis 60/86, glioma 9/153)', fontsize=6.5, va='center', linespacing=1.3)
    # panel 3: bars
    x0 = xs[2]
    n_r = sum(v for k, v in rc.items() if k) + risk_unstated
    vox = rc.get('Voxel', 0); les = rc.get('Lesion', 0)
    ax.text(x0 + PAD, 58, 'Primary studies with a risk-estimation\nmethod (n = %d), by evaluation unit' % n_r, fontsize=6.5, va='top', linespacing=1.3)
    rows3 = [('Voxel level only', vox, CATEGORICAL[0]), ('Lesion level', les, ACCENT_RED), ('Estimates risk that a lesion is missed', 0, ACCENT_RED)]
    for i, (lab, v, col) in enumerate(rows3):
        y = 41 - i * 11
        ax.text(x0 + PAD, y + 3.2, lab, fontsize=6.0, va='bottom')
        ax.add_patch(plt.Rectangle((x0 + PAD, y - 2), 36 * v / n_r, 4, fc=col, ec='none'))
        ax.text(x0 + PAD + 36 * v / n_r + 1.5, y, '%d / %d' % (v, n_r), fontsize=6.5, va='center')
    ax.text(x0 + PAD, 10, 'Report the evaluation unit and\nlesion-matching rules.', fontsize=6.5, fontweight='bold', va='center', linespacing=1.3, color=BLACK)
    for xa in (xs[0] + w, xs[1] + w):
        arrow(ax, xa + .4, 38, xa + 5.6, 38)
    save_cns_figure(fig, os.path.join(OUT, 'graphical_abstract'))
    plt.close(fig)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    fig_prisma()
    fig_graphical()
    mm = 1 / 25.4
    fig = plt.figure(figsize=(183 * mm, 121 * mm))
    gs = gridspec.GridSpec(2, 2, width_ratios=[1.35, 1.0], height_ratios=[1.0, 1.0], wspace=0.62, hspace=0.95,
                           left=0.135, right=0.975, top=0.90, bottom=0.145, figure=fig)
    axa = fig.add_subplot(gs[:, 0]); axb = fig.add_subplot(gs[0, 1]); axc = fig.add_subplot(gs[1, 1])
    panel_heat(axa); panel_risk(axb); panel_size(axc)
    fig.canvas.draw()
    bbs = {k: ax.get_tightbbox(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted()) for k, ax in (('a', axa), ('b', axb), ('c', axc))}
    xbc = min(bbs['b'].x0, bbs['c'].x0)
    for k in 'abc':
        fig.text((bbs[k].x0 if k == 'a' else xbc) - 0.005, bbs[k].y1 + 0.01, k, fontsize=9, fontweight='bold', va='bottom', ha='right')
    save_cns_figure(fig, os.path.join(OUT, 'fig2_units_risk_size'))
    print('heatmap n =', int(M.sum()), 'of', len(full), 'full-text; unit unknown', unit_unknown)
    print('risk', dict(rc)); print('size', size_rows)
