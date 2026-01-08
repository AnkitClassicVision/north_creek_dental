/**
 * North Creek Dental - Marketing Dashboard
 * Main JavaScript
 */

(function() {
  'use strict';

  // --------------------------------------------------------------------------
  // DOM Ready
  // --------------------------------------------------------------------------
  document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
    initScrollAnimations();
    initTabs();
    initProgressBars();
    initCountUp();
  });

  // --------------------------------------------------------------------------
  // Navigation
  // --------------------------------------------------------------------------
  function initNavigation() {
    const nav = document.querySelector('.nav');
    const toggle = document.querySelector('.nav__toggle');
    const links = document.querySelector('.nav__links');

    // Mobile menu toggle
    if (toggle && links) {
      toggle.addEventListener('click', function() {
        links.classList.toggle('nav__links--open');
        const isOpen = links.classList.contains('nav__links--open');
        toggle.setAttribute('aria-expanded', isOpen);
      });

      // Close menu when clicking a link
      links.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', function() {
          links.classList.remove('nav__links--open');
          toggle.setAttribute('aria-expanded', 'false');
        });
      });
    }

    // Scroll behavior - add background on scroll
    if (nav) {
      let lastScroll = 0;
      window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
          nav.style.background = 'rgba(10, 10, 15, 0.95)';
        } else {
          nav.style.background = 'rgba(10, 10, 15, 0.8)';
        }

        lastScroll = currentScroll;
      }, { passive: true });
    }

    // Set active nav link based on current page
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav__link').forEach(function(link) {
      const href = link.getAttribute('href');
      if (href === currentPath || (currentPath === '' && href === 'index.html')) {
        link.classList.add('nav__link--active');
      }
    });
  }

  // --------------------------------------------------------------------------
  // Scroll Animations
  // --------------------------------------------------------------------------
  function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('[data-animate]');

    if (!animatedElements.length) return;

    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    animatedElements.forEach(function(el) {
      observer.observe(el);
    });
  }

  // --------------------------------------------------------------------------
  // Tabs
  // --------------------------------------------------------------------------
  function initTabs() {
    const tabContainers = document.querySelectorAll('.tabs');

    tabContainers.forEach(function(container) {
      const tabs = container.querySelectorAll('.tabs__tab');
      const contents = container.querySelectorAll('.tabs__content');

      tabs.forEach(function(tab) {
        tab.addEventListener('click', function() {
          const target = this.getAttribute('data-tab');

          // Update active tab
          tabs.forEach(function(t) {
            t.classList.remove('tabs__tab--active');
          });
          this.classList.add('tabs__tab--active');

          // Update active content
          contents.forEach(function(content) {
            content.classList.remove('tabs__content--active');
            if (content.getAttribute('data-tab-content') === target) {
              content.classList.add('tabs__content--active');
            }
          });
        });
      });
    });
  }

  // --------------------------------------------------------------------------
  // Progress Bars
  // --------------------------------------------------------------------------
  function initProgressBars() {
    const progressBars = document.querySelectorAll('.progress__fill');

    if (!progressBars.length) return;

    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          const fill = entry.target;
          const value = fill.getAttribute('data-value');
          fill.style.width = value + '%';
          observer.unobserve(fill);
        }
      });
    }, { threshold: 0.5 });

    progressBars.forEach(function(bar) {
      bar.style.width = '0%';
      observer.observe(bar);
    });
  }

  // --------------------------------------------------------------------------
  // Count Up Animation
  // --------------------------------------------------------------------------
  function initCountUp() {
    const counters = document.querySelectorAll('[data-count]');

    if (!counters.length) return;

    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          const counter = entry.target;
          const target = parseFloat(counter.getAttribute('data-count'));
          const suffix = counter.getAttribute('data-suffix') || '';
          const prefix = counter.getAttribute('data-prefix') || '';
          const decimals = counter.getAttribute('data-decimals') || 0;
          const duration = 2000;
          const startTime = performance.now();

          function updateCount(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Easing function
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const current = target * easeOut;

            counter.textContent = prefix + current.toFixed(decimals) + suffix;

            if (progress < 1) {
              requestAnimationFrame(updateCount);
            } else {
              counter.textContent = prefix + target.toFixed(decimals) + suffix;
            }
          }

          requestAnimationFrame(updateCount);
          observer.unobserve(counter);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(function(counter) {
      observer.observe(counter);
    });
  }

  // --------------------------------------------------------------------------
  // Utility Functions
  // --------------------------------------------------------------------------

  // Smooth scroll to element
  window.smoothScrollTo = function(target) {
    const element = document.querySelector(target);
    if (element) {
      const offset = 100;
      const position = element.getBoundingClientRect().top + window.pageYOffset - offset;
      window.scrollTo({
        top: position,
        behavior: 'smooth'
      });
    }
  };

  // Format currency
  window.formatCurrency = function(value) {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0
    }).format(value);
  };

  // Format percentage
  window.formatPercent = function(value) {
    return value.toFixed(1) + '%';
  };

})();
