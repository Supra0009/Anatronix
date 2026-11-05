import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Anatonix | Dual-Engine Biomechanical & Ocular Guardian",
    page_icon="🦴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            border: none !important;
            width: 100% !important;
            height: 100vh !important;
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

anatonix_html = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anatonix | Unified Biomechanical & Ocular Guardian</title>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <!-- FontAwesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Dual Vision Engines: MediaPipe Pose + Face Mesh -->
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/pose/pose.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh.js" crossorigin="anonymous"></script>

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            cyberDark: '#070A10',
            cyberSurface: '#0E1626',
            cyberCard: '#131E33',
            cyberBorder: '#1F2C47',
            neonGreen: '#10B981',
            neonCyan: '#06B6D4',
            neonAmber: '#F59E0B',
            neonCrimson: '#EF4444',
            neonPurple: '#A855F7'
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            display: ['Chakra Petch', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },
          boxShadow: {
            'glow-cyan': '0 0 20px -4px rgba(6, 182, 212, 0.45)',
            'glow-crimson': '0 0 25px -2px rgba(239, 68, 68, 0.6)',
            'glow-emerald': '0 0 20px -4px rgba(16, 185, 129, 0.45)',
          }
        }
      }
    }
  </script>

  <style>
    .hud-grid {
      background-size: 26px 26px;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    }
    .custom-scrollbar::-webkit-scrollbar { width: 5px; height: 5px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: #090E17; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 9999px; }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #334155; }
    @keyframes pulse-intense {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.85; transform: scale(1.015); }
    }
    .shout-pulse { animation: pulse-intense 0.65s infinite ease-in-out; }
    input[type=range] { accent-color: #06B6D4; }
  </style>
</head>

<body class="bg-cyberDark text-slate-100 font-sans min-h-screen flex flex-col selection:bg-cyan-500 selection:text-black">

  <!-- Header -->
  <header class="border-b border-cyberBorder bg-cyberSurface/90 backdrop-blur-md sticky top-0 z-40 px-4 lg:px-8 py-2.5">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="relative flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-600 via-indigo-600 to-emerald-500 text-black shadow-glow-cyan">
          <i class="fa-solid fa-bone text-lg text-white"></i>
          <span class="absolute -top-1 -right-1 flex h-3 w-3">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
          </span>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="font-display font-bold text-xl tracking-wider text-white">ANATONIX</span>
            <span class="px-1.5 py-0.5 text-[10px] uppercase font-mono font-bold bg-cyan-950/80 border border-cyan-500/40 text-cyan-400 rounded">DUAL-ENGINE CV</span>
          </div>
          <p class="text-xs text-slate-400 font-mono tracking-tight hidden sm:block">Pose 3D Biomechanics + 468-pt Face Mesh Ocular Guardian</p>
        </div>
      </div>

      <div class="flex items-center gap-2.5">
        <div id="tabStatusPill" class="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-cyberDark/80 border border-cyberBorder text-xs font-mono">
          <div id="tabStatusDot" class="w-2.5 h-2.5 rounded-full bg-emerald-400"></div>
          <span id="tabStatusText" class="text-slate-300">ACTIVE</span>
        </div>

        <button id="btnAudioToggle" class="px-3 py-1.5 rounded-lg bg-emerald-950/80 border border-emerald-500/50 text-emerald-300 text-xs font-mono font-bold transition flex items-center gap-1.5 shadow-glow-emerald">
          <i id="audioIcon" class="fa-solid fa-volume-high"></i>
          <span id="audioText">VOICE: ON</span>
        </button>

        <button id="btnDownloadCSV" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 text-xs font-mono transition flex items-center gap-1.5">
          <i class="fa-solid fa-file-arrow-down"></i>
          <span class="hidden md:inline">Export CSV</span>
        </button>

        <button id="btnToggleCam" class="px-4 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-black text-xs font-mono font-bold transition flex items-center gap-1.5 shadow-glow-cyan">
          <i class="fa-solid fa-power-off"></i>
          <span id="btnToggleCamText">Start Optics</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Main Viewport -->
  <main class="max-w-7xl mx-auto w-full p-4 lg:p-6 flex-1 flex flex-col gap-5">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-5">
      
      <!-- Video Feed & HUD (7 cols) -->
      <div class="lg:col-span-7 flex flex-col gap-3">
        <div id="videoWrapper" class="relative w-full aspect-[4/3] bg-cyberDark border border-cyberBorder rounded-2xl overflow-hidden shadow-2xl flex items-center justify-center">
          <div class="absolute inset-0 hud-grid opacity-35 pointer-events-none"></div>

          <video id="webcam" class="hidden" playsinline autoplay muted></video>
          <canvas id="outputCanvas" class="w-full h-full object-cover z-10"></canvas>

          <!-- Standby Screen -->
          <div id="cameraStandbyScreen" class="absolute inset-0 z-20 bg-cyberDark/95 flex flex-col items-center justify-center p-6 text-center">
            <div class="w-16 h-16 rounded-2xl bg-cyan-950/60 border border-cyan-500/30 flex items-center justify-center text-cyan-400 mb-3 shadow-glow-cyan">
              <i class="fa-solid fa-crosshairs text-2xl"></i>
            </div>
            <h3 class="text-base font-display font-bold text-white mb-1">Dual-Engine Vision Link Standby</h3>
            <p class="text-xs text-slate-400 max-w-sm mb-4 font-mono">Parallel spinal posture tracking + 468-point corneal blink rate with background audio alerts.</p>
            <div class="flex flex-wrap gap-2 justify-center">
              <button id="btnStartCamera" class="px-5 py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-emerald-500 text-black font-display font-bold text-xs tracking-wider uppercase hover:opacity-90 shadow-glow-cyan transition">
                Initialize Video Link
              </button>
              <button id="btnSimulationMode" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-mono text-xs transition">
                Virtual Demo
              </button>
            </div>
          </div>

          <!-- Live Multi-Vector HUD Badges -->
          <div id="hudOverlay" class="absolute inset-0 z-15 pointer-events-none p-3 flex flex-col justify-between hidden">
            <div class="flex items-center justify-between">
              <div id="hudPostureBadge" class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-emerald-950/80 border border-emerald-500/50 text-emerald-400 font-mono text-[11px] backdrop-blur-md">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span id="hudPostureStatusText">POSTURE NORMAL</span>
              </div>
              <div id="hudBlinkBadge" class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-cyan-950/80 border border-cyan-500/50 text-cyan-300 font-mono text-[11px] backdrop-blur-md">
                <i class="fa-solid fa-eye"></i>
                <span id="hudBlinkStatusText">CORNEAL FILM: NOMINAL</span>
              </div>
            </div>

            <!-- Central Slouch Warning Banner -->
            <div id="hudWarningBox" class="self-center hidden px-6 py-2.5 rounded-xl bg-rose-950/95 border-2 border-rose-500 text-rose-300 font-mono text-center shadow-glow-crimson shout-pulse">
              <div class="text-xs uppercase font-bold tracking-widest text-white flex items-center justify-center gap-2">
                <i class="fa-solid fa-triangle-exclamation text-rose-400"></i> POSTURE COMPROMISED
              </div>
              <div class="text-xl font-display font-black text-white" id="hudOffsetBigText">+16° FORWARD LEAN</div>
              <div class="text-[10px] text-rose-300">SIT BACK. FIX YOUR POSTURE.</div>
            </div>

            <div class="flex items-end justify-between font-mono text-[10px]">
              <div class="bg-cyberDark/85 backdrop-blur-md p-2 rounded-lg border border-cyberBorder space-y-0.5">
                <div>CERVICAL LEAN: <span id="hudFwdLean" class="text-cyan-400 font-bold">0°</span></div>
                <div>SHOULDER TILT: <span id="hudShoulderTilt" class="text-amber-400 font-bold">0°</span></div>
                <div>Z-PROXIMITY: <span id="hudProximity" class="text-emerald-400 font-bold">1.00x</span></div>
              </div>
              <div class="flex items-center gap-2">
                <div id="hudCooldownBadge" class="hidden px-2.5 py-1 rounded bg-slate-900/90 border border-slate-700 text-amber-400">
                  COOLDOWN: <span id="hudCooldownTimer">0.0s</span>
                </div>
                <button id="btnCalibrateInline" class="pointer-events-auto px-3 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-black font-display font-bold text-xs uppercase shadow transition">
                  Calibrate ('c')
                </button>
              </div>
            </div>
          </div>

          <div id="slouchBorderEffect" class="absolute inset-0 pointer-events-none rounded-2xl border-4 border-transparent transition-all duration-200 z-18"></div>
        </div>

        <div class="flex items-center justify-between bg-cyberCard border border-cyberBorder px-3 py-2 rounded-xl text-xs font-mono">
          <div class="flex items-center gap-3">
            <span class="text-slate-400">Dual Vision:</span>
            <span class="text-cyan-400 font-bold">Pose (33) + FaceMesh (468)</span>
          </div>
          <div class="flex items-center gap-4">
            <button id="btnToggleSkeleton" class="text-cyan-400 hover:text-cyan-300 transition" title="Toggle Vector HUD">
              <i class="fa-solid fa-network-wired"></i> Vectors
            </button>
            <span id="metricFps" class="text-emerald-400 font-bold">30 FPS</span>
          </div>
        </div>
      </div>

      <!-- Right Column: Ocular PIP + Biomechanical Symmetry (5 cols) -->
      <div class="lg:col-span-5 flex flex-col gap-4">
        
        <!-- Live Ocular PIP Box -->
        <div class="bg-cyberCard border border-cyberBorder rounded-2xl p-4 shadow-xl">
          <div class="flex items-center justify-between mb-2">
            <div class="flex items-center gap-2">
              <i class="fa-solid fa-eye-low-vision text-cyan-400 text-sm"></i>
              <span class="text-xs font-mono uppercase font-bold text-slate-300">Isolated Ocular PIP</span>
            </div>
            <span id="eyeStateBadge" class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/40">EYES OPEN</span>
          </div>

          <div class="relative w-full h-32 bg-cyberDark rounded-xl overflow-hidden border border-cyberBorder flex items-center justify-center">
            <canvas id="eyeCanvas" class="w-full h-full object-cover"></canvas>
            <div class="absolute top-2 right-2 px-1.5 py-0.5 bg-cyberDark/80 rounded border border-cyberBorder text-[9px] font-mono text-slate-400">
              EAR: <span id="valEarCurrent" class="text-cyan-400 font-bold">0.00</span>
            </div>
          </div>

          <div class="grid grid-cols-3 gap-2 mt-3 text-center">
            <div class="bg-cyberSurface p-2 rounded-lg border border-cyberBorder/60">
              <span class="text-[9px] font-mono uppercase text-slate-400 block">Total Blinks</span>
              <span id="statBlinkCount" class="font-display font-bold text-lg text-cyan-400">0</span>
            </div>
            <div class="bg-cyberSurface p-2 rounded-lg border border-cyberBorder/60">
              <span class="text-[9px] font-mono uppercase text-slate-400 block">Blink Rate</span>
              <div class="flex items-baseline justify-center gap-0.5">
                <span id="statBpm" class="font-display font-bold text-lg text-emerald-400">0.0</span>
                <span class="text-[9px] text-slate-400 font-mono">BPM</span>
              </div>
            </div>
            <div class="bg-cyberSurface p-2 rounded-lg border border-cyberBorder/60">
              <span class="text-[9px] font-mono uppercase text-slate-400 block">Dry Eye Index</span>
              <span id="statDryEyeRisk" class="font-display font-bold text-xs text-emerald-400 mt-1 block">OPTIMAL</span>
            </div>
          </div>
        </div>

        <!-- Biomechanical Symmetry & Cervical Load Gauges -->
        <div class="bg-cyberCard border border-cyberBorder rounded-2xl p-4 shadow-xl flex-1 flex flex-col justify-between">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-mono uppercase font-bold text-slate-300">Biomechanical Symmetry</span>
            <span id="calibStatusLabel" class="text-[10px] font-mono text-cyan-400">Uncalibrated</span>
          </div>

          <div class="grid grid-cols-2 gap-2 text-xs font-mono">
            <div class="bg-cyberSurface p-2.5 rounded-xl border border-cyberBorder">
              <span class="text-slate-400 block text-[10px] uppercase">Cervical Pitch</span>
              <div class="flex items-baseline justify-between mt-1">
                <span id="statLeanDeg" class="font-display font-bold text-lg text-slate-100">0.0°</span>
                <span id="statLeanVerdict" class="text-[10px] text-emerald-400 font-bold">UPRIGHT</span>
              </div>
            </div>

            <div class="bg-cyberSurface p-2.5 rounded-xl border border-cyberBorder">
              <span class="text-slate-400 block text-[10px] uppercase">Shoulder Slope</span>
              <div class="flex items-baseline justify-between mt-1">
                <span id="statShoulderDeg" class="font-display font-bold text-lg text-slate-100">0.0°</span>
                <span id="statShoulderVerdict" class="text-[10px] text-emerald-400 font-bold">LEVEL</span>
              </div>
            </div>

            <div class="bg-cyberSurface p-2.5 rounded-xl border border-cyberBorder">
              <span class="text-slate-400 block text-[10px] uppercase">Screen Proximity</span>
              <div class="flex items-baseline justify-between mt-1">
                <span id="statProximityVal" class="font-display font-bold text-lg text-slate-100">1.00x</span>
                <span id="statProximityVerdict" class="text-[10px] text-emerald-400 font-bold">OPTIMAL</span>
              </div>
            </div>

            <div class="bg-cyberSurface p-2.5 rounded-xl border border-cyberBorder">
              <span class="text-slate-400 block text-[10px] uppercase">Cervical Load</span>
              <div class="flex items-baseline justify-between mt-1">
                <span id="statCervicalLoad" class="font-display font-bold text-lg text-slate-100">10 lbs</span>
                <span class="text-[10px] text-slate-400">Spine torque</span>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-2 mt-3 text-xs font-mono">
            <div class="p-2 rounded-xl bg-cyberSurface border border-cyberBorder flex items-center justify-between">
              <span class="text-slate-400">Good Time %:</span>
              <span id="statGoodPercentage" class="font-bold text-emerald-400">100%</span>
            </div>
            <div class="p-2 rounded-xl bg-cyberSurface border border-cyberBorder flex items-center justify-between">
              <span class="text-slate-400">Slouch Events:</span>
              <span id="statSlouchEvents" class="font-bold text-rose-400">0</span>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- Controls Panel: Audio Synthesis, Sensitivity & Event Stream -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      
      <!-- Audio Engine Config -->
      <div class="bg-cyberCard border border-cyberBorder rounded-2xl p-4 shadow-xl flex flex-col justify-between">
        <div>
          <div class="flex items-center gap-2 mb-3">
            <div class="w-8 h-8 rounded-lg bg-rose-950/60 border border-rose-500/40 text-rose-400 flex items-center justify-center">
              <i class="fa-solid fa-bullhorn text-sm"></i>
            </div>
            <div>
              <h4 class="font-display font-bold text-sm text-white">Voice & Shouting Engine</h4>
              <p class="text-[10px] text-slate-400 font-mono">Web AudioContext Keep-Alive Support</p>
            </div>
          </div>

          <div class="space-y-3 text-xs font-mono">
            <div>
              <label class="block text-slate-400 mb-1">Audio Urgency Mode:</label>
              <select id="selectSpeechMode" class="w-full bg-cyberSurface border border-cyberBorder rounded-lg px-2.5 py-1.5 text-slate-200">
                <option value="shout">Urgent Shout ("Sit back. Fix your posture.")</option>
                <option value="stern">Stern Biomechanical ("Posture compromised.")</option>
                <option value="custom">Custom Template Phrasing</option>
              </select>
            </div>

            <div id="customPhraseContainer" class="hidden">
              <label class="block text-slate-400 mb-1">Custom Alert ({deg} supported):</label>
              <input type="text" id="inputCustomPhrase" value="Sit back! Leaning forward by {deg} degrees!" class="w-full bg-cyberSurface border border-cyberBorder rounded-lg px-2.5 py-1.5 text-slate-200 text-xs">
            </div>

            <div>
              <label class="block text-slate-400 mb-1">Synthesizer Voice:</label>
              <select id="selectVoice" class="w-full bg-cyberSurface border border-cyberBorder rounded-lg px-2.5 py-1 text-slate-200 text-xs truncate">
                <option value="">System Default Voice</option>
              </select>
            </div>

            <div class="grid grid-cols-2 gap-3 pt-1">
              <div>
                <div class="flex justify-between text-[10px] mb-1">
                  <span class="text-slate-400">Speech Rate</span>
                  <span id="labelSpeechRate" class="text-cyan-400">1.25x</span>
                </div>
                <input type="range" id="rangeSpeechRate" min="0.8" max="2.0" step="0.05" value="1.25" class="w-full cursor-pointer">
              </div>
              <div>
                <div class="flex justify-between text-[10px] mb-1">
                  <span class="text-slate-400">Pitch Urgency</span>
                  <span id="labelSpeechPitch" class="text-cyan-400">1.1</span>
                </div>
                <input type="range" id="rangeSpeechPitch" min="0.5" max="1.5" step="0.1" value="1.1" class="w-full cursor-pointer">
              </div>
            </div>
          </div>
        </div>

        <button id="btnTestVoiceAlert" class="mt-3 w-full py-2 rounded-xl bg-cyberSurface hover:bg-slate-800 border border-slate-700 text-slate-200 text-xs font-mono font-medium transition flex items-center justify-center gap-2">
          <i class="fa-solid fa-play text-cyan-400"></i> Test Audio Shout Trigger
        </button>
      </div>

      <!-- Detection Sensitivity & Presets -->
      <div class="bg-cyberCard border border-cyberBorder rounded-2xl p-4 shadow-xl flex flex-col justify-between">
        <div>
          <div class="flex items-center gap-2 mb-3">
            <div class="w-8 h-8 rounded-lg bg-cyan-950/60 border border-cyan-500/40 text-cyan-400 flex items-center justify-center">
              <i class="fa-solid fa-sliders text-sm"></i>
            </div>
            <div>
              <h4 class="font-display font-bold text-sm text-white">Sensitivity & Thresholds</h4>
              <p class="text-[10px] text-slate-400 font-mono">Biomechanical Trigger Limits</p>
            </div>
          </div>

          <div class="space-y-3.5 text-xs font-mono">
            <div>
              <div class="flex justify-between mb-1">
                <span class="text-slate-300">Forward Lean Tolerance:</span>
                <span id="labelThreshold" class="text-amber-400 font-bold">12.0°</span>
              </div>
              <input type="range" id="rangeThreshold" min="5" max="30" step="0.5" value="12.0" class="w-full cursor-pointer">
              <div class="flex justify-between text-[9px] text-slate-400 mt-0.5">
                <span>Strict (7°)</span>
                <span>Standard (12°)</span>
                <span>Lenient (22°)</span>
              </div>
            </div>

            <div>
              <div class="flex justify-between mb-1">
                <span class="text-slate-300">Sustained Slouch Delay:</span>
                <span id="labelFrameDelay" class="text-cyan-400 font-bold">0.8s (25 frames)</span>
              </div>
              <input type="range" id="rangeFrameDelay" min="10" max="90" step="5" value="25" class="w-full cursor-pointer">
            </div>

            <div>
              <div class="flex justify-between mb-1">
                <span class="text-slate-300">Shout Cooldown Delay:</span>
                <span id="labelCooldown" class="text-emerald-400 font-bold">3.0s</span>
              </div>
              <input type="range" id="rangeCooldown" min="1.0" max="8.0" step="0.5" value="3.0" class="w-full cursor-pointer">
            </div>
          </div>
        </div>

        <div class="pt-2 border-t border-cyberBorder flex items-center justify-between text-[11px] font-mono text-slate-400">
          <span>Presets:</span>
          <div class="flex gap-1.5">
            <button id="presetStrict" class="px-2 py-0.5 rounded bg-cyberSurface hover:bg-slate-800 text-slate-300">Strict</button>
            <button id="presetStandard" class="px-2 py-0.5 rounded bg-cyan-950 text-cyan-400 border border-cyan-500/30">Standard</button>
            <button id="presetLenient" class="px-2 py-0.5 rounded bg-cyberSurface hover:bg-slate-800 text-slate-300">Lenient</button>
          </div>
        </div>
      </div>

      <!-- Telemetry Stream & Diagnostics -->
      <div class="bg-cyberCard border border-cyberBorder rounded-2xl p-4 shadow-xl flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-2">
            <div class="flex items-center gap-2">
              <div class="w-8 h-8 rounded-lg bg-emerald-950/60 border border-emerald-500/40 text-emerald-400 flex items-center justify-center">
                <i class="fa-solid fa-list-check text-sm"></i>
              </div>
              <div>
                <h4 class="font-display font-bold text-sm text-white">Event Log Stream</h4>
                <p class="text-[10px] text-slate-400 font-mono">Auditory & Vision Events</p>
              </div>
            </div>
            <button id="btnClearLog" class="text-slate-400 hover:text-white text-xs font-mono">
              <i class="fa-solid fa-trash-can"></i>
            </button>
          </div>

          <div id="eventLogContainer" class="h-44 bg-cyberDark rounded-xl p-2.5 border border-cyberBorder font-mono text-[10px] overflow-y-auto space-y-1.5 custom-scrollbar">
            <div class="text-slate-400 flex items-start gap-1.5">
              <span class="text-cyan-400">[INIT]</span>
              <span>Anatonix dual-engine CV guardian initialized.</span>
            </div>
          </div>
        </div>

        <div class="pt-2 border-t border-cyberBorder flex items-center justify-between text-[11px] font-mono text-slate-400">
          <span>Session Elapsed:</span>
          <span id="statSessionTimer" class="text-cyan-400 font-bold">00:00</span>
        </div>
      </div>

    </div>

    <!-- Real-Time Trend Graph -->
    <div class="w-full bg-cyberCard rounded-2xl p-4 border border-cyberBorder shadow-xl flex flex-col gap-2">
      <div class="flex flex-wrap items-center justify-between text-xs font-mono gap-2">
        <span class="text-slate-300 font-bold">Real-Time Ergonomic Variance Stream (60-Sec Rolling Window)</span>
        <div class="flex items-center gap-3 text-[10px]">
          <span class="text-cyan-400">■ Forward Lean (deg)</span>
          <span class="text-amber-400">■ Shoulder Tilt (deg)</span>
          <span class="text-purple-400">■ EAR (x100)</span>
        </div>
      </div>
      <div class="relative w-full h-24 bg-cyberDark rounded-xl overflow-hidden border border-cyberBorder">
        <canvas id="analyticsChartCanvas" class="w-full h-full"></canvas>
      </div>
    </div>

  </main>

  <script>
    const state = {
      isCameraRunning: false,
      isSimulationMode: false,
      isAudioMuted: false,
      drawSkeleton: true,

      // Thresholds
      pitchToleranceDeg: 12.0,
      badPostureFrameLimit: 25,
      cooldownSeconds: 3.0,

      // Calibration baselines
      baselinePitch: null,
      baselineShoulderSlope: null,
      baselineShoulderWidth: null,
      isCalibrated: false,

      // Live metrics
      rawPitch: 0.0,
      forwardLeanAngle: 0.0,
      shoulderTiltAngle: 0.0,
      proximityRatio: 1.0,
      cervicalLoadLbs: 10,
      slouchCount: 0,
      badPostureFrames: 0,
      cooldownTimer: 0,

      // Ocular metrics
      blinkCount: 0,
      isEyeClosed: false,
      blinkTimestamps: [],
      currentEar: 0.28,
      dryEyeRisk: "OPTIMAL",

      // Speech engine
      speechRate: 1.25,
      speechPitch: 1.1,
      speechMode: 'shout',
      customPhrase: "Sit back! Leaning forward by {deg} degrees!",
      selectedVoiceIndex: 0,

      // Session telemetry
      sessionStartTime: null,
      totalFramesProcessed: 0,
      goodFramesProcessed: 0,
      records: [],
      lastLogTime: 0,
      lastChartUpdate: 0,
      simTime: 0
    };

    // Keep-alive Audio Oscillator
    let audioCtx = null;
    let silentOscillator = null;

    function initAudioKeepAlive() {
      try {
        if (!audioCtx) {
          const AudioContextClass = window.AudioContext || window.webkitAudioContext;
          if (AudioContextClass) {
            audioCtx = new AudioContextClass();
            silentOscillator = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();
            gainNode.gain.value = 0.00001; // inaudible
            silentOscillator.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            silentOscillator.start();
            logEvent('AUDIO', 'Silent background keep-alive oscillator armed.');
          }
        }
        if (audioCtx && audioCtx.state === 'suspended') {
          audioCtx.resume();
        }
      } catch (e) {
        console.warn('AudioContext keep-alive warning:', e);
      }
    }

    // DOM Elements
    const videoEl = document.getElementById('webcam');
    const canvasEl = document.getElementById('outputCanvas');
    const ctx = canvasEl.getContext('2d');
    const eyeCanvas = document.getElementById('eyeCanvas');
    const eyeCtx = eyeCanvas.getContext('2d');
    const chartCanvas = document.getElementById('analyticsChartCanvas');
    const chartCtx = chartCanvas.getContext('2d');

    const cameraStandbyScreen = document.getElementById('cameraStandbyScreen');
    const hudOverlay = document.getElementById('hudOverlay');
    const hudPostureBadge = document.getElementById('hudPostureBadge');
    const hudPostureStatusText = document.getElementById('hudPostureStatusText');
    const hudBlinkBadge = document.getElementById('hudBlinkBadge');
    const hudBlinkStatusText = document.getElementById('hudBlinkStatusText');
    const hudWarningBox = document.getElementById('hudWarningBox');
    const hudOffsetBigText = document.getElementById('hudOffsetBigText');
    const slouchBorderEffect = document.getElementById('slouchBorderEffect');
    const hudCooldownBadge = document.getElementById('hudCooldownBadge');
    const hudCooldownTimer = document.getElementById('hudCooldownTimer');

    const hudFwdLean = document.getElementById('hudFwdLean');
    const hudShoulderTilt = document.getElementById('hudShoulderTilt');
    const hudProximity = document.getElementById('hudProximity');

    const eyeStateBadge = document.getElementById('eyeStateBadge');
    const valEarCurrent = document.getElementById('valEarCurrent');
    const statBlinkCount = document.getElementById('statBlinkCount');
    const statBpm = document.getElementById('statBpm');
    const statDryEyeRisk = document.getElementById('statDryEyeRisk');

    const calibStatusLabel = document.getElementById('calibStatusLabel');
    const statLeanDeg = document.getElementById('statLeanDeg');
    const statLeanVerdict = document.getElementById('statLeanVerdict');
    const statShoulderDeg = document.getElementById('statShoulderDeg');
    const statShoulderVerdict = document.getElementById('statShoulderVerdict');
    const statProximityVal = document.getElementById('statProximityVal');
    const statProximityVerdict = document.getElementById('statProximityVerdict');
    const statCervicalLoad = document.getElementById('statCervicalLoad');
    const statGoodPercentage = document.getElementById('statGoodPercentage');
    const statSlouchEvents = document.getElementById('statSlouchEvents');
    const statSessionTimer = document.getElementById('statSessionTimer');
    const metricFps = document.getElementById('metricFps');

    const tabStatusDot = document.getElementById('tabStatusDot');
    const tabStatusText = document.getElementById('tabStatusText');
    const eventLogContainer = document.getElementById('eventLogContainer');

    const btnStartCamera = document.getElementById('btnStartCamera');
    const btnToggleCam = document.getElementById('btnToggleCam');
    const btnToggleCamText = document.getElementById('btnToggleCamText');
    const btnSimulationMode = document.getElementById('btnSimulationMode');
    const btnAudioToggle = document.getElementById('btnAudioToggle');
    const audioIcon = document.getElementById('audioIcon');
    const audioText = document.getElementById('audioText');
    const btnCalibrateInline = document.getElementById('btnCalibrateInline');
    const btnToggleSkeleton = document.getElementById('btnToggleSkeleton');
    const btnDownloadCSV = document.getElementById('btnDownloadCSV');
    const btnTestVoiceAlert = document.getElementById('btnTestVoiceAlert');
    const btnClearLog = document.getElementById('btnClearLog');

    const rangeThreshold = document.getElementById('rangeThreshold');
    const labelThreshold = document.getElementById('labelThreshold');
    const rangeFrameDelay = document.getElementById('rangeFrameDelay');
    const labelFrameDelay = document.getElementById('labelFrameDelay');
    const rangeCooldown = document.getElementById('rangeCooldown');
    const labelCooldown = document.getElementById('labelCooldown');

    const selectSpeechMode = document.getElementById('selectSpeechMode');
    const customPhraseContainer = document.getElementById('customPhraseContainer');
    const inputCustomPhrase = document.getElementById('inputCustomPhrase');
    const selectVoice = document.getElementById('selectVoice');
    const rangeSpeechRate = document.getElementById('rangeSpeechRate');
    const labelSpeechRate = document.getElementById('labelSpeechRate');
    const rangeSpeechPitch = document.getElementById('rangeSpeechPitch');
    const labelSpeechPitch = document.getElementById('labelSpeechPitch');

    const presetStrict = document.getElementById('presetStrict');
    const presetStandard = document.getElementById('presetStandard');
    const presetLenient = document.getElementById('presetLenient');

    let poseModel = null;
    let faceMeshModel = null;
    let animationFrameId = null;
    let bgInterval = null;
    let isProcessing = false;
    let latestPoseLandmarks = null;
    let lastFrameTime = performance.now();
    let fpsSmoothed = 30;
    let voicesList = [];

    // Web Speech Alert Engine
    function initSpeechEngine() {
      if (!('speechSynthesis' in window)) {
        logEvent('WARN', 'Web Speech API unavailable in browser.');
        return;
      }
      function populateVoices() {
        voicesList = window.speechSynthesis.getVoices();
        selectVoice.innerHTML = '';
        voicesList.forEach((voice, index) => {
          const opt = document.createElement('option');
          opt.value = index;
          opt.textContent = `${voice.name} (${voice.lang})${voice.default ? ' — [Default]' : ''}`;
          selectVoice.appendChild(opt);
        });

        const preferredIndex = voicesList.findIndex(v => 
          (v.lang.includes('en-US') || v.lang.includes('en-GB')) && 
          (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Daniel') || v.name.includes('David'))
        );
        if (preferredIndex !== -1) {
          selectVoice.value = preferredIndex;
          state.selectedVoiceIndex = preferredIndex;
        }
      }
      populateVoices();
      if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = populateVoices;
      }
    }

    function triggerAudioShout(forwardDegrees) {
      if (state.isAudioMuted || !('speechSynthesis' in window)) return;
      if (window.speechSynthesis.speaking) return;

      initAudioKeepAlive();

      const degRounded = Math.max(0, Math.round(forwardDegrees));
      let message = "Sit back. Fix your posture.";

      if (state.speechMode === 'shout') {
        const phrases = [
          "Sit back. Fix your posture.",
          `Sit straight! Forward tilt is ${degRounded} degrees!`,
          "Fix your posture! Spine is curving forward!"
        ];
        message = phrases[Math.floor(Math.random() * phrases.length)];
      } else if (state.speechMode === 'stern') {
        message = `Posture compromised. Lean offset is ${degRounded} degrees.`;
      } else if (state.speechMode === 'custom') {
        message = state.customPhrase.replace('{deg}', degRounded);
      }

      try {
        const utter = new SpeechSynthesisUtterance(message);
        if (voicesList[state.selectedVoiceIndex]) {
          utter.voice = voicesList[state.selectedVoiceIndex];
        }
        utter.rate = state.speechRate;
        utter.pitch = state.speechPitch;
        utter.volume = 1.0;
        window.speechSynthesis.speak(utter);
        logEvent('SHOUT', `Audio alert: "${message}"`);
      } catch (err) {
        console.error('Speech synthesis error:', err);
      }
    }

    function logEvent(tag, text) {
      const now = new Date();
      const timeStr = now.toTimeString().split(' ')[0];
      const entry = document.createElement('div');
      entry.className = "flex items-start gap-1.5 text-slate-300";

      let tagColor = "text-cyan-400";
      if (tag === 'WARN') tagColor = "text-amber-400";
      if (tag === 'SHOUT') tagColor = "text-rose-400";
      if (tag === 'CALIB') tagColor = "text-emerald-400";
      if (tag === 'BG') tagColor = "text-purple-400";

      entry.innerHTML = `<span class="${tagColor}">[${tag}]</span><span class="text-slate-400">${timeStr}</span><span>${text}</span>`;
      eventLogContainer.prepend(entry);

      if (eventLogContainer.children.length > 50) {
        eventLogContainer.removeChild(eventLogContainer.lastChild);
      }
    }

    // Vision Models Init
    async function initEngines() {
      poseModel = new Pose({
        locateFile: (f) => `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${f}`
      });
      poseModel.setOptions({
        modelComplexity: 1,
        smoothLandmarks: true,
        minDetectionConfidence: 0.5,
        minTrackingConfidence: 0.5
      });
      poseModel.onResults(onPoseResults);

      faceMeshModel = new FaceMesh({
        locateFile: (f) => `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/${f}`
      });
      faceMeshModel.setOptions({
        maxNumFaces: 1,
        refineLandmarks: true,
        minDetectionConfidence: 0.5,
        minTrackingConfidence: 0.5
      });
      faceMeshModel.onResults(onFaceMeshResults);

      logEvent('INIT', 'Pose 3D and 468-pt Face Mesh engines loaded.');
    }

    function onPoseResults(res) {
      latestPoseLandmarks = res.poseLandmarks || null;
    }

    function calculateEAR(p, top1, top2, bot1, bot2, left, right) {
      const v1 = Math.hypot(p[top1].x - p[bot1].x, p[top1].y - p[bot1].y);
      const v2 = Math.hypot(p[top2].x - p[bot2].x, p[top2].y - p[bot2].y);
      const h = Math.hypot(p[left].x - p[right].x, p[left].y - p[right].y);
      return (v1 + v2) / (2.0 * Math.max(h, 0.001));
    }

    function onFaceMeshResults(res) {
      if (!state.isCameraRunning && !state.isSimulationMode) return;

      const isHidden = document.hidden;
      const w = canvasEl.width = videoEl.videoWidth || 640;
      const h = canvasEl.height = videoEl.videoHeight || 480;

      if (!isHidden && videoEl.readyState >= 2) {
        ctx.save();
        ctx.clearRect(0, 0, w, h);
        ctx.translate(w, 0);
        ctx.scale(-1, 1);
        ctx.drawImage(videoEl, 0, 0, w, h);
        ctx.restore();
      }

      // 1. Process Ocular Mesh
      if (res.multiFaceLandmarks && res.multiFaceLandmarks.length > 0) {
        const face = res.multiFaceLandmarks[0];

        const earLeft = calculateEAR(face, 160, 158, 144, 153, 33, 133);
        const earRight = calculateEAR(face, 385, 387, 380, 373, 362, 263);
        const earAvg = (earLeft + earRight) / 2.0;
        state.currentEar = earAvg;
        valEarCurrent.textContent = earAvg.toFixed(3);

        const BLINK_THRESH = 0.19;
        if (earAvg < BLINK_THRESH && !state.isEyeClosed) {
          state.isEyeClosed = true;
          state.blinkCount++;
          state.blinkTimestamps.push(Date.now());
          statBlinkCount.textContent = state.blinkCount;

          eyeStateBadge.textContent = "BLINK";
          eyeStateBadge.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-cyan-950 text-cyan-400 border border-cyan-500/40";
        } else if (earAvg >= BLINK_THRESH && state.isEyeClosed) {
          state.isEyeClosed = false;
          eyeStateBadge.textContent = "EYES OPEN";
          eyeStateBadge.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/40";
        }

        if (!isHidden) {
          cropEyesToPIP(face, w, h);
        }
      }

      // 2. Process Biomechanical Pose
      if (latestPoseLandmarks) {
        processPoseBiometrics(latestPoseLandmarks, w, h, isHidden);
      }

      updateOcularDiagnostics();
      updateTelemetryLog();
      updateDashboardStats();

      // FPS Calculation
      const now = performance.now();
      const dt = (now - lastFrameTime) / 1000;
      lastFrameTime = now;
      if (dt > 0) {
        fpsSmoothed = 0.9 * fpsSmoothed + 0.1 * (1 / dt);
        metricFps.textContent = `${Math.round(fpsSmoothed)} FPS`;
      }
    }

    function cropEyesToPIP(face, w, h) {
      const lOuter = face[33];
      const rOuter = face[263];
      const nose = face[168];

      const eyeWidthNorm = Math.hypot(rOuter.x - lOuter.x, rOuter.y - lOuter.y);
      const cropW = Math.max(0.18, eyeWidthNorm * 1.8) * w;
      const cropH = cropW * 0.42;

      const cx = ((lOuter.x + rOuter.x) / 2) * w;
      const cy = nose.y * h;

      const sx = Math.max(0, Math.min(w - cropW, cx - cropW / 2));
      const sy = Math.max(0, Math.min(h - cropH, cy - cropH / 2));

      eyeCanvas.width = 320;
      eyeCanvas.height = 135;

      eyeCtx.save();
      eyeCtx.translate(320, 0);
      eyeCtx.scale(-1, 1);
      eyeCtx.drawImage(videoEl, sx, sy, cropW, cropH, 0, 0, 320, 135);
      eyeCtx.restore();

      eyeCtx.strokeStyle = state.isEyeClosed ? '#06B6D4' : 'rgba(6, 182, 212, 0.4)';
      eyeCtx.lineWidth = 2;
      eyeCtx.strokeRect(8, 8, 304, 119);
    }

    function processPoseBiometrics(landmarks, w, h, isHidden) {
      const lEar = landmarks[7];
      const rEar = landmarks[8];
      const lSh = landmarks[11];
      const rSh = landmarks[12];

      if (!lEar || !rEar || !lSh || !rSh) return;

      const earMid = {
        x: (lEar.x + rEar.x) / 2,
        y: (lEar.y + rEar.y) / 2,
        z: ((lEar.z || 0) + (rEar.z || 0)) / 2
      };
      const shMid = {
        x: (lSh.x + rSh.x) / 2,
        y: (lSh.y + rSh.y) / 2,
        z: ((lSh.z || 0) + (rSh.z || 0)) / 2
      };

      const dy = shMid.y - earMid.y;
      const dz = shMid.z - earMid.z;
      const rawPitch = Math.atan2(dz * 100, Math.max(dy * 100, 1.0)) * (180 / Math.PI);
      const rawSlope = Math.atan2(rSh.y - lSh.y, rSh.x - lSh.x) * (180 / Math.PI);
      const shoulderSpan = Math.hypot(rSh.x - lSh.x, rSh.y - lSh.y);

      state.rawPitch = rawPitch;

      // Calibration initialization
      if (!state.isCalibrated) {
        state.baselinePitch = rawPitch;
        state.baselineShoulderSlope = rawSlope;
        state.baselineShoulderWidth = shoulderSpan;
        state.isCalibrated = true;
        calibStatusLabel.textContent = `Baseline Set (${rawPitch.toFixed(1)}°)`;
        logEvent('CALIB', `Calibrated upright baseline pitch to ${rawPitch.toFixed(1)}°.`);
      }

      state.forwardLeanAngle = Math.max(0, rawPitch - state.baselinePitch);
      state.shoulderTiltAngle = Math.abs(rawSlope - (state.baselineShoulderSlope || 0));
      state.proximityRatio = shoulderSpan / (state.baselineShoulderWidth || shoulderSpan);

      // Kapandji cervical spinal load estimation
      let lbs = 10;
      if (state.forwardLeanAngle > 28) lbs = 49;
      else if (state.forwardLeanAngle > 18) lbs = 32;
      else if (state.forwardLeanAngle > 8) lbs = 22;
      state.cervicalLoadLbs = lbs;

      if (!isHidden && state.drawSkeleton) {
        drawSkeletalVectors(earMid, shMid, lSh, rSh, w, h);
      }

      evaluatePostureGuardian();
    }

    function drawSkeletalVectors(earMid, shMid, lSh, rSh, w, h) {
      const earX = (1 - earMid.x) * w;
      const earY = earMid.y * h;
      const shX = (1 - shMid.x) * w;
      const shY = shMid.y * h;
      const lShX = (1 - lSh.x) * w;
      const lShY = lSh.y * h;
      const rShX = (1 - rSh.x) * w;
      const rShY = rSh.y * h;

      const isBadLean = state.forwardLeanAngle > state.pitchToleranceDeg;
      const isBadTilt = state.shoulderTiltAngle > 6.0;

      // Cervical Vector
      ctx.beginPath();
      ctx.strokeStyle = isBadLean ? '#EF4444' : '#06B6D4';
      ctx.lineWidth = 4;
      ctx.moveTo(shX, shY);
      ctx.lineTo(earX, earY);
      ctx.stroke();

      ctx.fillStyle = '#06B6D4';
      ctx.beginPath(); ctx.arc(shX, shY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = isBadLean ? '#EF4444' : '#10B981';
      ctx.beginPath(); ctx.arc(earX, earY, 7, 0, Math.PI * 2); ctx.fill();

      // Shoulder Vector
      ctx.beginPath();
      ctx.strokeStyle = isBadTilt ? '#F59E0B' : '#10B981';
      ctx.lineWidth = 3;
      ctx.moveTo(lShX, lShY);
      ctx.lineTo(rShX, rShY);
      ctx.stroke();

      ctx.fillStyle = isBadTilt ? '#F59E0B' : '#10B981';
      ctx.beginPath(); ctx.arc(lShX, lShY, 5, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(rShX, rShY, 5, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#FFFFFF";
      ctx.font = "bold 12px 'JetBrains Mono', monospace";
      ctx.shadowColor = "rgba(0,0,0,0.8)";
      ctx.shadowBlur = 5;
      ctx.fillText(`+${Math.round(state.forwardLeanAngle)}°`, earX + 12, earY - 4);
      ctx.shadowBlur = 0;
    }

    function evaluatePostureGuardian() {
      state.totalFramesProcessed++;

      hudFwdLean.textContent = `+${Math.round(state.forwardLeanAngle)}°`;
      hudShoulderTilt.textContent = `${state.shoulderTiltAngle.toFixed(1)}°`;
      hudProximity.textContent = `${state.proximityRatio.toFixed(2)}x`;

      statLeanDeg.textContent = `${state.forwardLeanAngle.toFixed(1)}°`;
      statShoulderDeg.textContent = `${state.shoulderTiltAngle.toFixed(1)}°`;
      statProximityVal.textContent = `${state.proximityRatio.toFixed(2)}x`;
      statCervicalLoad.textContent = `${state.cervicalLoadLbs} lbs`;

      const isSlouch = state.forwardLeanAngle > state.pitchToleranceDeg || state.shoulderTiltAngle > 6.0;

      if (isSlouch) {
        state.badPostureFrames++;
        statLeanVerdict.textContent = state.forwardLeanAngle > state.pitchToleranceDeg ? "SLOUCH" : "UPRIGHT";
        statLeanVerdict.className = state.forwardLeanAngle > state.pitchToleranceDeg ? "text-[10px] text-rose-400 font-bold" : "text-[10px] text-emerald-400 font-bold";
        
        statShoulderVerdict.textContent = state.shoulderTiltAngle > 6.0 ? "UNEVEN" : "LEVEL";
        statShoulderVerdict.className = state.shoulderTiltAngle > 6.0 ? "text-[10px] text-amber-400 font-bold" : "text-[10px] text-emerald-400 font-bold";

        if (state.badPostureFrames > state.badPostureFrameLimit) {
          hudPostureBadge.className = "flex items-center gap-1.5 px-2.5 py-1 rounded bg-rose-950/80 border border-rose-500/70 text-rose-400 font-mono text-[11px] backdrop-blur-md shadow-glow-crimson";
          hudPostureStatusText.textContent = "WARNING: SLOUCHING";
          hudWarningBox.classList.remove('hidden');
          hudOffsetBigText.textContent = `+${Math.round(state.forwardLeanAngle)}° FORWARD LEAN`;
          slouchBorderEffect.className = "absolute inset-0 pointer-events-none rounded-2xl border-4 border-rose-500 shadow-glow-crimson transition-all duration-200 z-18";

          if (state.cooldownTimer <= 0) {
            state.slouchCount++;
            statSlouchEvents.textContent = state.slouchCount;
            triggerAudioShout(state.forwardLeanAngle);
            state.cooldownTimer = state.cooldownSeconds;
          }
        }
      } else {
        state.goodFramesProcessed++;
        state.badPostureFrames = Math.max(0, state.badPostureFrames - 1);
        statLeanVerdict.textContent = "UPRIGHT";
        statLeanVerdict.className = "text-[10px] text-emerald-400 font-bold";
        statShoulderVerdict.textContent = "LEVEL";
        statShoulderVerdict.className = "text-[10px] text-emerald-400 font-bold";

        hudWarningBox.classList.add('hidden');
        slouchBorderEffect.className = "absolute inset-0 pointer-events-none rounded-2xl border-4 border-transparent transition-all duration-200 z-18";
        hudPostureBadge.className = "flex items-center gap-1.5 px-2.5 py-1 rounded bg-emerald-950/80 border border-emerald-500/50 text-emerald-400 font-mono text-[11px] backdrop-blur-md";
        hudPostureStatusText.textContent = "POSTURE NORMAL";
      }

      if (state.cooldownTimer > 0) {
        state.cooldownTimer = Math.max(0, state.cooldownTimer - 0.033);
        hudCooldownBadge.classList.remove('hidden');
        hudCooldownTimer.textContent = `${state.cooldownTimer.toFixed(1)}s`;
      } else {
        hudCooldownBadge.classList.add('hidden');
      }
    }

    function updateOcularDiagnostics() {
      const oneMinuteAgo = Date.now() - 60000;
      state.blinkTimestamps = state.blinkTimestamps.filter(t => t > oneMinuteAgo);
      const bpm = state.blinkTimestamps.length;
      statBpm.textContent = bpm.toFixed(1);

      if (bpm < 8 && state.blinkCount > 5) {
        state.dryEyeRisk = "HIGH RISK";
        statDryEyeRisk.className = "font-display font-bold text-xs text-rose-500 mt-1 block";
        hudBlinkBadge.className = "flex items-center gap-1.5 px-2.5 py-1 rounded bg-rose-950/80 border border-rose-500/50 text-rose-400 font-mono text-[11px] backdrop-blur-md";
        hudBlinkStatusText.textContent = "DRY EYE ALERT (<8 BPM)";
      } else if (bpm < 12 && state.blinkCount > 5) {
        state.dryEyeRisk = "MILD STRAIN";
        statDryEyeRisk.className = "font-display font-bold text-xs text-amber-400 mt-1 block";
        hudBlinkBadge.className = "flex items-center gap-1.5 px-2.5 py-1 rounded bg-amber-950/80 border border-amber-500/50 text-amber-400 font-mono text-[11px] backdrop-blur-md";
        hudBlinkStatusText.textContent = "CORNEAL REHYDRATION NEEDED";
      } else {
        state.dryEyeRisk = "OPTIMAL";
        statDryEyeRisk.className = "font-display font-bold text-xs text-emerald-400 mt-1 block";
        hudBlinkBadge.className = "flex items-center gap-1.5 px-2.5 py-1 rounded bg-cyan-950/80 border border-cyan-500/50 text-cyan-300 font-mono text-[11px] backdrop-blur-md";
        hudBlinkStatusText.textContent = "CORNEAL FILM: NOMINAL";
      }
      statDryEyeRisk.textContent = state.dryEyeRisk;
    }

    function updateTelemetryLog() {
      const now = Date.now();
      if (now - state.lastLogTime >= 1000) {
        state.lastLogTime = now;
        state.records.push({
          timestamp: new Date().toISOString(),
          forwardLean: state.forwardLeanAngle.toFixed(1),
          shoulderTilt: state.shoulderTiltAngle.toFixed(1),
          earVal: state.currentEar.toFixed(3),
          proximity: state.proximityRatio.toFixed(2),
          cervicalLoad: state.cervicalLoadLbs,
          bpm: state.blinkTimestamps.length,
          dryEyeRisk: state.dryEyeRisk,
          status: (state.forwardLeanAngle > state.pitchToleranceDeg || state.shoulderTiltAngle > 6) ? 'BAD' : 'GOOD'
        });

        if (state.records.length > 1800) state.records.shift();
      }
    }

    function updateDashboardStats() {
      if (state.totalFramesProcessed > 0) {
        const pct = Math.round((state.goodFramesProcessed / state.totalFramesProcessed) * 100);
        statGoodPercentage.textContent = `${pct}%`;
      }
      if (state.sessionStartTime) {
        const diffMs = Date.now() - state.sessionStartTime;
        const totalSecs = Math.floor(diffMs / 1000);
        const mins = String(Math.floor(totalSecs / 60)).padStart(2, '0');
        const secs = String(totalSecs % 60).padStart(2, '0');
        statSessionTimer.textContent = `${mins}:${secs}`;
      }

      const now = performance.now();
      if (now - state.lastChartUpdate > 1000) {
        state.lastChartUpdate = now;
        if (!document.hidden) renderChart();
      }
    }

    function renderChart() {
      const w = chartCanvas.width = chartCanvas.parentElement.clientWidth;
      const h = chartCanvas.height = chartCanvas.parentElement.clientHeight;
      chartCtx.clearRect(0, 0, w, h);

      if (state.records.length < 2) return;
      const slice = state.records.slice(-60);
      const stepX = w / (slice.length - 1);

      // Tolerance horizontal guide line
      const threshY = h - (state.pitchToleranceDeg / 35) * h;
      chartCtx.beginPath();
      chartCtx.strokeStyle = 'rgba(245, 158, 11, 0.4)';
      chartCtx.setLineDash([3, 3]);
      chartCtx.moveTo(0, threshY);
      chartCtx.lineTo(w, threshY);
      chartCtx.stroke();
      chartCtx.setLineDash([]);

      // Forward lean line (Cyan)
      chartCtx.beginPath();
      chartCtx.strokeStyle = '#06B6D4';
      chartCtx.lineWidth = 1.8;
      slice.forEach((r, i) => {
        const y = h - (Math.min(35, r.forwardLean) / 35) * h;
        if (i === 0) chartCtx.moveTo(0, y);
        else chartCtx.lineTo(i * stepX, y);
      });
      chartCtx.stroke();

      // Shoulder tilt line (Amber)
      chartCtx.beginPath();
      chartCtx.strokeStyle = '#F59E0B';
      chartCtx.lineWidth = 1.5;
      slice.forEach((r, i) => {
        const y = h - (Math.min(15, r.shoulderTilt) / 15) * h;
        if (i === 0) chartCtx.moveTo(0, y);
        else chartCtx.lineTo(i * stepX, y);
      });
      chartCtx.stroke();

      // EAR Line (Purple)
      chartCtx.beginPath();
      chartCtx.strokeStyle = '#A855F7';
      chartCtx.lineWidth = 1.2;
      slice.forEach((r, i) => {
        const y = h - (Math.min(0.4, r.earVal) / 0.4) * h;
        if (i === 0) chartCtx.moveTo(0, y);
        else chartCtx.lineTo(i * stepX, y);
      });
      chartCtx.stroke();
    }

    // Camera Loops & Frame Execution
    async function processCurrentDualFrame() {
      if ((!state.isCameraRunning && !state.isSimulationMode) || isProcessing) return;
      if (videoEl.readyState < 2 || !poseModel || !faceMeshModel) return;

      isProcessing = true;
      try {
        await poseModel.send({ image: videoEl });
        await faceMeshModel.send({ image: videoEl });
      } catch (err) {
        console.error('Frame processing error:', err);
      } finally {
        isProcessing = false;
      }
    }

    function renderLoop() {
      if (state.isCameraRunning && !document.hidden) {
        processCurrentDualFrame().then(() => {
          if (state.isCameraRunning && !document.hidden) {
            animationFrameId = requestAnimationFrame(renderLoop);
          }
        });
      }
    }

    document.addEventListener("visibilitychange", () => {
      if (document.hidden) {
        tabStatusDot.className = "w-2.5 h-2.5 rounded-full bg-purple-400 animate-pulse";
        tabStatusText.textContent = "BACKGROUND";
        logEvent('BG', 'Tab hidden: Switched to 16FPS interval worker.');

        if (animationFrameId) {
          cancelAnimationFrame(animationFrameId);
          animationFrameId = null;
        }

        initAudioKeepAlive();

        if (!bgInterval && state.isCameraRunning) {
          bgInterval = setInterval(() => {
            if (state.isCameraRunning && videoEl.readyState >= 2) {
              processCurrentDualFrame();
            }
          }, 60);
        }
      } else {
        tabStatusDot.className = "w-2.5 h-2.5 rounded-full bg-emerald-400";
        tabStatusText.textContent = "ACTIVE";
        logEvent('INFO', 'Tab active: Resuming smooth animation loop.');

        if (bgInterval) {
          clearInterval(bgInterval);
          bgInterval = null;
        }
        if (state.isCameraRunning) {
          animationFrameId = requestAnimationFrame(renderLoop);
        }
      }
    });

    async function startOptics() {
      if (state.isCameraRunning) return;
      stopSimulation();
      initAudioKeepAlive();

      try {
        logEvent('INFO', 'Opening camera for dual posture + corneal tracking...');
        const stream = await navigator.mediaDevices.getUserMedia({
          video: { width: { ideal: 640 }, height: { ideal: 480 }, facingMode: 'user' },
          audio: false
        });
        videoEl.srcObject = stream;
        await videoEl.play();

        state.isCameraRunning = true;
        state.sessionStartTime = Date.now();
        cameraStandbyScreen.classList.add('hidden');
        hudOverlay.classList.remove('hidden');
        btnToggleCamText.textContent = "Stop Optics";

        logEvent('INFO', 'Optics link active. Sit straight and press "c" to zero baseline.');

        if (document.hidden) {
          bgInterval = setInterval(() => {
            if (state.isCameraRunning && videoEl.readyState >= 2) {
              processCurrentDualFrame();
            }
          }, 60);
        } else {
          animationFrameId = requestAnimationFrame(renderLoop);
        }
      } catch (err) {
        logEvent('WARN', 'Camera link failed. Switching to virtual simulation mode.');
        startSimulation();
      }
    }

    function stopOptics() {
      if (bgInterval) {
        clearInterval(bgInterval);
        bgInterval = null;
      }
      if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
      }
      if (videoEl.srcObject) {
        videoEl.srcObject.getTracks().forEach(t => t.stop());
        videoEl.srcObject = null;
      }

      state.isCameraRunning = false;
      cameraStandbyScreen.classList.remove('hidden');
      hudOverlay.classList.add('hidden');
      btnToggleCamText.textContent = "Start Optics";
      logEvent('INFO', 'Camera optics feed stopped.');
    }

    function startSimulation() {
      stopOptics();
      initAudioKeepAlive();
      state.isSimulationMode = true;
      state.sessionStartTime = Date.now();
      cameraStandbyScreen.classList.add('hidden');
      hudOverlay.classList.remove('hidden');
      logEvent('INFO', 'Synthetic biomechanical simulation active.');

      function simLoop() {
        if (!state.isSimulationMode) return;
        state.simTime += 0.035;

        canvasEl.width = 640;
        canvasEl.height = 480;
        const w = 640;
        const h = 480;

        ctx.fillStyle = '#070A10';
        ctx.fillRect(0, 0, w, h);

        const simLean = (Math.sin(state.simTime) + 1) / 2;
        const mockZDepth = -0.15 * simLean;

        const mockLandmarks = [
          null, null, null, null, null, null, null,
          { x: 0.45, y: 0.35, z: mockZDepth },
          { x: 0.55, y: 0.35, z: mockZDepth },
          null, null,
          { x: 0.40, y: 0.60, z: 0.0 },
          { x: 0.60, y: 0.60, z: 0.0 }
        ];

        processPoseBiometrics(mockLandmarks, w, h, document.hidden);

        // Synthetic blink simulation
        if (Math.random() < 0.03 && !state.isEyeClosed) {
          state.isEyeClosed = true;
          state.blinkCount++;
          state.blinkTimestamps.push(Date.now());
          statBlinkCount.textContent = state.blinkCount;
        } else if (state.isEyeClosed) {
          state.isEyeClosed = false;
        }

        updateOcularDiagnostics();
        updateTelemetryLog();
        updateDashboardStats();

        animationFrameId = requestAnimationFrame(simLoop);
      }
      animationFrameId = requestAnimationFrame(simLoop);
    }

    function stopSimulation() {
      state.isSimulationMode = false;
      if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = null;
      }
    }

    function calibrateBaseline() {
      initAudioKeepAlive();
      state.baselinePitch = state.rawPitch;
      state.isCalibrated = true;
      calibStatusLabel.textContent = `Baseline Set (${state.baselinePitch.toFixed(1)}°)`;
      logEvent('CALIB', `Upright baseline pitch calibrated to ${state.baselinePitch.toFixed(1)}°. Forward lean zeroed.`);
    }

    function setPreset(thresh, delayFrames, cooldownSec) {
      state.pitchToleranceDeg = thresh;
      rangeThreshold.value = thresh;
      labelThreshold.textContent = `${thresh.toFixed(1)}°`;

      state.badPostureFrameLimit = delayFrames;
      rangeFrameDelay.value = delayFrames;
      labelFrameDelay.textContent = `${(delayFrames / 30).toFixed(1)}s (${delayFrames} frames)`;

      state.cooldownSeconds = cooldownSec;
      rangeCooldown.value = cooldownSec;
      labelCooldown.textContent = `${cooldownSec.toFixed(1)}s`;

      logEvent('INFO', `Preset applied: Tolerance ${thresh}°, Delay ${delayFrames}f, Cooldown ${cooldownSec}s`);
    }

    function exportCSV() {
      if (state.records.length === 0) {
        alert("No active session data collected yet.");
        return;
      }
      let csv = "Timestamp,ForwardLeanDeg,ShoulderTiltDeg,EAR,Proximity,CervicalLoadLbs,BlinksPerMin,DryEyeRisk,PostureStatus\\n";
      state.records.forEach(r => {
        csv += `${r.timestamp},${r.forwardLean},${r.shoulderTilt},${r.earVal},${r.proximity},${r.cervicalLoad},${r.bpm},${r.dryEyeRisk},${r.status}\\n`;
      });

      const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", `anatonix_telemetry_${Date.now()}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      logEvent('INFO', 'Telemetry log exported to CSV.');
    }

    function bindEvents() {
      window.addEventListener('keydown', (e) => {
        if (e.key === 'c' || e.key === 'C') calibrateBaseline();
        else if (e.key === 'q' || e.key === 'Q') {
          if (state.isCameraRunning) stopOptics();
        }
      });

      btnStartCamera.addEventListener('click', startOptics);
      btnToggleCam.addEventListener('click', () => {
        if (state.isCameraRunning || state.isSimulationMode) {
          stopOptics();
          stopSimulation();
        } else {
          startOptics();
        }
      });
      btnSimulationMode.addEventListener('click', startSimulation);
      btnCalibrateInline.addEventListener('click', calibrateBaseline);

      btnToggleSkeleton.addEventListener('click', () => {
        state.drawSkeleton = !state.drawSkeleton;
        btnToggleSkeleton.classList.toggle('text-cyan-400');
        btnToggleSkeleton.classList.toggle('text-slate-500');
      });

      btnAudioToggle.addEventListener('click', () => {
        state.isAudioMuted = !state.isAudioMuted;
        initAudioKeepAlive();
        if (state.isAudioMuted) {
          audioIcon.className = "fa-solid fa-volume-xmark";
          audioText.textContent = "VOICE: OFF";
          btnAudioToggle.className = "px-3 py-1.5 rounded-lg bg-rose-950/80 border border-rose-500/50 text-rose-300 text-xs font-mono font-bold transition flex items-center gap-1.5";
          logEvent('WARN', 'Audio shout alerts muted.');
        } else {
          audioIcon.className = "fa-solid fa-volume-high";
          audioText.textContent = "VOICE: ON";
          btnAudioToggle.className = "px-3 py-1.5 rounded-lg bg-emerald-950/80 border border-emerald-500/50 text-emerald-300 text-xs font-mono font-bold transition flex items-center gap-1.5 shadow-glow-emerald";
          logEvent('INFO', 'Audio shout alerts activated.');
        }
      });

      selectSpeechMode.addEventListener('change', (e) => {
        state.speechMode = e.target.value;
        customPhraseContainer.classList.toggle('hidden', state.speechMode !== 'custom');
      });
      inputCustomPhrase.addEventListener('input', (e) => {
        state.customPhrase = e.target.value;
      });
      selectVoice.addEventListener('change', (e) => {
        state.selectedVoiceIndex = parseInt(e.target.value);
      });
      rangeSpeechRate.addEventListener('input', (e) => {
        state.speechRate = parseFloat(e.target.value);
        labelSpeechRate.textContent = `${state.speechRate.toFixed(2)}x`;
      });
      rangeSpeechPitch.addEventListener('input', (e) => {
        state.speechPitch = parseFloat(e.target.value);
        labelSpeechPitch.textContent = state.speechPitch.toFixed(1);
      });

      rangeThreshold.addEventListener('input', (e) => {
        state.pitchToleranceDeg = parseFloat(e.target.value);
        labelThreshold.textContent = `${state.pitchToleranceDeg.toFixed(1)}°`;
      });
      rangeFrameDelay.addEventListener('input', (e) => {
        state.badPostureFrameLimit = parseInt(e.target.value);
        labelFrameDelay.textContent = `${(state.badPostureFrameLimit / 30).toFixed(1)}s (${state.badPostureFrameLimit} frames)`;
      });
      rangeCooldown.addEventListener('input', (e) => {
        state.cooldownSeconds = parseFloat(e.target.value);
        labelCooldown.textContent = `${state.cooldownSeconds.toFixed(1)}s`;
      });

      presetStrict.addEventListener('click', () => setPreset(7.0, 15, 2.0));
      presetStandard.addEventListener('click', () => setPreset(12.0, 25, 3.0));
      presetLenient.addEventListener('click', () => setPreset(18.0, 35, 4.0));

      btnTestVoiceAlert.addEventListener('click', () => {
        initAudioKeepAlive();
        triggerAudioShout(18.0);
      });
      btnDownloadCSV.addEventListener('click', exportCSV);
      btnClearLog.addEventListener('click', () => {
        eventLogContainer.innerHTML = '';
        logEvent('INFO', 'Event stream cleared.');
      });
    }

    window.addEventListener('DOMContentLoaded', () => {
      initSpeechEngine();
      initEngines();
      bindEvents();
    });
  </script>
</body>
</html>
"""

components.html(anatonix_html, height=1050, scrolling=True)