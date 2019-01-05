# pysmartapp
[![Build Status](https://travis-ci.org/andrewsayre/pysmartapp.svg?branch=master)](https://travis-ci.org/andrewsayre/pysmartapp)
[![Coverage Status](https://coveralls.io/repos/github/andrewsayre/pysmartapp/badge.svg?branch=master)](https://coveralls.io/github/andrewsayre/pysmartapp?branch=master)
[![image](https://img.shields.io/pypi/v/pysmartapp.svg)](https://pypi.org/project/pysmartapp/)
[![image](https://img.shields.io/pypi/pyversions/pysmartapp.svg)](https://pypi.org/project/pysmartapp/)
[![image](https://img.shields.io/pypi/l/pysmartapp.svg)](https://pypi.org/project/pysmartapp/)
[![image](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)

A python implementation of the WebHook-based [SmartThings SmartApp](https://smartthings.developer.samsung.com/develop/guides/smartapps/basics.html) that uses asyncio and the dispatcher pattern to notify callbacks (coroutines or functions) of SmartApp lifecycle events.