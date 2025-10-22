import os

# lazy loader and safe fallback for CI
_summarizer = None
_summarizer_loaded = False

def _load_summarizer():
	"""
	Attempt to load the transformers pipeline unless the environment
	indicates we should skip (CI or SKIP_MODEL). Returns pipeline or None.
	"""
	global _summarizer, _summarizer_loaded
	if _summarizer_loaded:
		return _summarizer
	_summarizer_loaded = True

	# Skip heavy model load in CI or when explicitly requested
	if os.getenv("CI") or os.getenv("SKIP_MODEL"):
		_summarizer = None
		return None

	try:
		from transformers import pipeline
		_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
	except Exception:
		# If model cannot be loaded, fall back to None
		_summarizer = None
	return _summarizer

def summarize_text(text, max_summary_len: int = 200):
	"""
	Return a summary. If the heavy model isn't available, return a short
	truncation of the original text as a safe fallback.
	"""
	if not text:
		return ""
	# ensure summarizer is attempted only when needed
	s = _load_summarizer()
	if s is None:
		# safe, deterministic fallback: first max_summary_len chars
		trim = text.strip()
		if len(trim) <= max_summary_len:
			return trim
		return trim[:max_summary_len].rsplit(" ", 1)[0] + "..."
	# Use the model
	try:
		result = s(text, max_length=50, min_length=25, do_sample=False)
		return result[0].get('summary_text', '').strip()
	except Exception:
		# On runtime model error, fallback
		trim = text.strip()
		if len(trim) <= max_summary_len:
			return trim
		return trim[:max_summary_len].rsplit(" ", 1)[0] + "..."
