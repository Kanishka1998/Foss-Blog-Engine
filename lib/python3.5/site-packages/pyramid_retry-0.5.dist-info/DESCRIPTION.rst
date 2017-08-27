=============
pyramid_retry
=============

.. image:: https://img.shields.io/pypi/v/pyramid_retry.svg
    :target: https://pypi.python.org/pypi/pyramid_retry

.. image:: https://img.shields.io/travis/Pylons/pyramid_retry/master.svg
    :target: https://travis-ci.org/Pylons/pyramid_retry

.. image:: https://readthedocs.org/projects/pyramid_retry/badge/?version=latest
    :target: https://readthedocs.org/projects/pyramid_retry/?badge=latest
    :alt: Documentation Status

``pyramid_retry`` is an execution policy for Pyramid that wraps requests and
can retry them a configurable number of times under certain "retryable" error
conditions before indicating a failure to the client.

See http://docs.pylonsproject.org/projects/pyramid-retry/en/latest/
or ``docs/index.rst`` in this distribution for detailed
documentation.


0.5 (2017-06-19)
================

- Update the policy to to track changes in Pyramid 1.9b1. This is an
  incompatible change and requires at least Pyramid 1.9b1.
  See https://github.com/Pylons/pyramid_retry/pull/11

0.4 (2017-06-12)
================

- Add the ``mark_error_retryable`` function in order to easily mark
  certain errors as retryable for ``pyramid_retry`` to detect.
  See https://github.com/Pylons/pyramid_retry/pull/8

- Add the ``IBeforeRetry`` event that can be subscribed to be notified
  when a retry is about to occur in order to perform cleanup on the
  ``environ``. See https://github.com/Pylons/pyramid_retry/pull/9

0.3 (2017-04-10)
================

- Support a ``retry.activate_hook`` setting which can return a per-request
  number of retries. See https://github.com/Pylons/pyramid_retry/pull/4

- Configuration is deferred so that settings may be changed after
  ``config.include('pyramid_retry')`` is invoked until the configurator
  is committed. See https://github.com/Pylons/pyramid_retry/pull/4

- Rename the view predicates to ``last_retry_attempt`` and
  ``retryable_error``. See https://github.com/Pylons/pyramid_retry/pull/3

- Rename ``pyramid_retry.is_exc_retryable`` to
  ``pyramid_retry.is_error_retryable``.
  See https://github.com/Pylons/pyramid_retry/pull/3

0.2 (2017-03-02)
================

- Change the default attempts to 3 instead of 1.

- Rename the view predicates to ``is_last_attempt`` and ``is_exc_retryable``.

- Drop support for the ``tm.attempts`` setting.

- The ``retry.attempts`` setting is always set now in
  ``registry.settings['retry.attempts']`` so that apps can inspect it.

0.1 (2017-03-01)
================

- Initial release.


