/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./frontend/scss/globals.scss":
/*!************************************!*\
  !*** ./frontend/scss/globals.scss ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n\n\n//# sourceURL=webpack://penny/./frontend/scss/globals.scss?");

/***/ }),

/***/ "./frontend/scripts/animations/typewriter.ts":
/*!***************************************************!*\
  !*** ./frontend/scripts/animations/typewriter.ts ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\nvar typewriter = function (element, text, delay) {\n    var i = 0;\n    var type = function () {\n        if (i < text.length) {\n            element.innerHTML += text.charAt(i);\n            i++;\n            setTimeout(type, delay);\n        }\n    };\n    type();\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (typewriter);\n\n\n//# sourceURL=webpack://penny/./frontend/scripts/animations/typewriter.ts?");

/***/ }),

/***/ "./frontend/scripts/helpers/idSelector.ts":
/*!************************************************!*\
  !*** ./frontend/scripts/helpers/idSelector.ts ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\nvar idSelector = function (id) { return document.getElementById(id); };\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (idSelector);\n\n\n//# sourceURL=webpack://penny/./frontend/scripts/helpers/idSelector.ts?");

/***/ }),

/***/ "./frontend/scripts/index.ts":
/*!***********************************!*\
  !*** ./frontend/scripts/index.ts ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _helpers_idSelector__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./helpers/idSelector */ \"./frontend/scripts/helpers/idSelector.ts\");\n/* harmony import */ var _animations_typewriter__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./animations/typewriter */ \"./frontend/scripts/animations/typewriter.ts\");\n/* harmony import */ var _scss_globals_scss__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../scss/globals.scss */ \"./frontend/scss/globals.scss\");\n\n\n\nwindow.addEventListener(\"load\", function () {\n    var helloElement = (0,_helpers_idSelector__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(\"typewriter\");\n    if (helloElement) {\n        var text = helloElement.textContent;\n        helloElement.style.display = \"block\";\n        helloElement.innerHTML = \"\";\n        (0,_animations_typewriter__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(helloElement, text, 10);\n    }\n    var switchThemeElement = (0,_helpers_idSelector__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(\"switch-theme\");\n    if (switchThemeElement) {\n        switchThemeElement.addEventListener(\"click\", function () {\n            document.documentElement.classList.toggle(\"dark\");\n        });\n    }\n});\n\n\n//# sourceURL=webpack://penny/./frontend/scripts/index.ts?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./frontend/scripts/index.ts");
/******/ 	
/******/ })()
;