# Import required libraries
import joblib
import ast
import tempfile
import subprocess
import ast
# Radon is used to calculate cyclomatic complexity

from radon.complexity import cc_visit
# Load trained ML model and vectorizer

model = joblib.load("models/bug_classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def ast_suggestions(code):
    suggestions = []

    try:
                # Parse source code into AST

        tree = ast.parse(code)
        # Walk through every node

        for node in ast.walk(tree):

            # Detect eval()
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id == "eval":
                        suggestions.append(
                            "Avoid eval(); use safer alternatives."
                        )

            # Detect == None
            if isinstance(node, ast.Compare):
                for comparator in node.comparators:
                    if isinstance(comparator, ast.Constant):
                        if comparator.value is None:
                            suggestions.append(
                                "Use 'is None' instead of '== None'."
                            )

            # Detect range(len())
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call):
                    if isinstance(node.iter.func, ast.Name):
                        if node.iter.func.id == "range":
                            suggestions.append(
                                "Check if direct iteration is possible instead of range()."
                            )

    except:
        pass

    return list(set(suggestions))

def check_syntax(code):
    try:
        ast.parse(code)
        return "No syntax errors"
    except SyntaxError as e:
        return f"Syntax Error: {e}"


def analyze_complexity(code):
    try:
        result = cc_visit(code)
        return [
            {
                "function": block.name,
                "complexity": block.complexity
            }
            for block in result
        ]
    except:
        return []


def security_scan(code):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
            temp.write(code.encode())
            temp_path = temp.name

        result = subprocess.run(
            ["py", "-m", "bandit", temp_path],
            capture_output=True,
            text=True
        )

        return result.stdout if result.stdout else "No issues found"

    except Exception as e:
        return f"Security scan failed: {str(e)}"
    
def predict_bug(code):
    X = vectorizer.transform([code])
    prediction = model.predict(X)[0]

    security = security_scan(code)

    if prediction == 1 and "Issue" in security:
        return "Potential bug/risky code detected"

    elif "Issue" in security:
        return "Security vulnerability detected"

    elif prediction == 1:
        return "Potential style/logic issue detected"

    return "Code looks clean"
def calculate_score(code, complexity, security, suggestions):
    score = 100

    if "Syntax Error" in check_syntax(code):
        score -= 40

    if complexity:
        for c in complexity:
            if c["complexity"] > 5:
                score -= 10

    if "Issue" in security:
        score -= 20

    score -= len(suggestions) * 5

    return max(score, 0)

def review_code(code):
    syntax = check_syntax(code)
    complexity = analyze_complexity(code)
    security = security_scan(code)
    bug_prediction = predict_bug(code)

    suggestions = ast_suggestions(code)
    
    if "Syntax Error" in syntax:
        suggestions.append(
            f"Fix syntax issue: {syntax}"
    )

    if "for" in code and "range(len(" in code:
        suggestions.append(
            "Use direct iteration instead of range(len())."
        )

    if "==" in code and "None" in code:
        suggestions.append(
            "Use 'is None' instead of '== None'."
        )

    if "eval(" in code:
        suggestions.append(
            "Avoid eval(); it may lead to security risks."
        )

    # MUST be after suggestions
    quality_score = calculate_score(
        code,
        complexity,
        security,
        suggestions
    )

    return {
        "syntax": syntax,
        "complexity": complexity,
        "security": security,
        "bug_prediction": bug_prediction,
        "quality_score": quality_score,
        "suggestions": suggestions
    }
def calculate_score(code, complexity, security, suggestions):
    score = 100

    if "Syntax Error" in check_syntax(code):
        score -= 40

    if complexity:
        for c in complexity:
            if c["complexity"] > 5:
                score -= 10

    if "Issue" in security:
        score -= 20

    score -= len(suggestions) * 5

    return max(score, 0)