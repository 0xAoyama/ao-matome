"""分類器 — カテゴリ/YMYL/著作権リスク/人物炎上リスクを判定"""

# 高リスクキーワード: 自動公開しない
HIGH_RISK_KEYWORDS = [
    "炎上", "不倫", "逮捕", "訴訟", "死亡", "事故",
    "詐欺", "暴露", "スキャンダル",
]

YMYL_KEYWORDS = [
    "医療", "健康", "投資", "税金", "確定申告", "保険",
    "給付金", "補助金", "年金", "ローン", "診断",
]

COPYRIGHT_RISK_KEYWORDS = [
    "歌詞", "全文", "ネタバレ", "漫画コマ", "転載",
]


def classify_risk(title: str, content: str = "") -> dict:
    """テキストからリスクレベルを判定する。"""
    text = (title + " " + content).lower()

    is_ymyl = any(kw in text for kw in YMYL_KEYWORDS)
    is_copyright_risk = any(kw in text for kw in COPYRIGHT_RISK_KEYWORDS)
    is_high_risk = any(kw in text for kw in HIGH_RISK_KEYWORDS)

    if is_high_risk:
        risk_level = "high"
    elif is_ymyl or is_copyright_risk:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "risk_level": risk_level,
        "ymyl": is_ymyl,
        "copyright_risk": is_copyright_risk,
    }
