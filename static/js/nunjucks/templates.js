(function () {
    (window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["templates/spinner.njk"] = (function () {
        function root(env, context, frame, runtime, cb) {
            var lineno = 0;
            var colno = 0;
            var output = "";
            try {
                var parentTemplate = null;
                output += "<div class=\"spinner-border\" role=\"status\">\n    <span class=\"sr-only\">Loading...</span>\n</div>";
                if (parentTemplate) {
                    parentTemplate.rootRenderFunc(env, context, frame, runtime, cb);
                } else {
                    cb(null, output);
                }
                ;
            } catch (e) {
                cb(runtime.handleError(e, lineno, colno));
            }
        }

        return {
            root: root
        };

    })();
})();

(function () {
    (window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["templates/todo.njk"] = (function () {
        function root(env, context, frame, runtime, cb) {
            var lineno = 0;
            var colno = 0;
            var output = "";
            try {
                var parentTemplate = null;
                output += "<td>";
                output += runtime.suppressValue(runtime.contextOrFrameLookup(context, frame, "quantity"), env.opts.autoescape);
                output += "</td>\n<td>";
                output += runtime.suppressValue(runtime.contextOrFrameLookup(context, frame, "name"), env.opts.autoescape);
                output += "</td>\n<td><a href=\"#\" class=\"btn btn-danger btn-sm delete\">X</a></td>\n";
                if (parentTemplate) {
                    parentTemplate.rootRenderFunc(env, context, frame, runtime, cb);
                } else {
                    cb(null, output);
                }
                ;
            } catch (e) {
                cb(runtime.handleError(e, lineno, colno));
            }
        }

        return {
            root: root
        };

    })();
})();

(function () {
    (window.nunjucksPrecompiled = window.nunjucksPrecompiled || {})["templates/todo-table.njk"] = (function () {
        function root(env, context, frame, runtime, cb) {
            var lineno = 0;
            var colno = 0;
            var output = "";
            try {
                var parentTemplate = null;
                output += " <table class=\"table table-striped mt-4\">\n    <thead>\n        <tr>\n            <th width=\"15%\">Quantity</th>\n            <th>Item</th>\n            <th width=\"15%\"></th>\n        </tr>\n    </thead>\n    <tbody id=\"item-list\"></tbody>\n</table>";
                if (parentTemplate) {
                    parentTemplate.rootRenderFunc(env, context, frame, runtime, cb);
                } else {
                    cb(null, output);
                }
                ;
            } catch (e) {
                cb(runtime.handleError(e, lineno, colno));
            }
        }

        return {
            root: root
        };

    })();
})();

