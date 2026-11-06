/* Cecil FC board dashboard.
   Soccer ball = truncated icosahedron (12 pentagons + 20 hexagons).
   Panels link to Google apps. /a/cecilfc.org is used where that host still
   opens the club account; other Workspace apps use ServiceLogin with hd=cecilfc.org.
   Jamboard is omitted — Google retired it. Drawings covers quick whiteboards.
*/
(function () {
  "use strict";

  var DOMAIN = "cecilfc.org";

  function hd(url) {
    return "https://accounts.google.com/ServiceLogin?hd=" + DOMAIN + "&continue=" + encodeURIComponent(url);
  }

  // Front of the ball first. The first nine are the ones the board asked for.
  var SERVICES = [
    { id: "gmail", label: "Gmail", name: "Gmail", group: "everyday", href: "https://mail.google.com/a/" + DOMAIN },
    { id: "calendar", label: "Calendar", name: "Calendar", group: "everyday", href: "https://calendar.google.com/a/" + DOMAIN },
    { id: "drive", label: "Drive", name: "Drive", group: "everyday", href: "https://drive.google.com/a/" + DOMAIN },
    { id: "docs", label: "Docs", name: "Docs", group: "everyday", href: "https://docs.google.com/a/" + DOMAIN },
    { id: "chat", label: "Chat", name: "Chat", group: "everyday", href: hd("https://chat.google.com/") },
    { id: "meet", label: "Meet", name: "Meet", group: "everyday", href: hd("https://meet.google.com/") },
    { id: "sheets", label: "Sheets", name: "Sheets", group: "everyday", href: hd("https://docs.google.com/spreadsheets/") },
    { id: "forms", label: "Forms", name: "Forms", group: "everyday", href: hd("https://docs.google.com/forms/") },
    { id: "keep", label: "Keep", name: "Keep", group: "everyday", href: "https://keep.google.com/a/" + DOMAIN + "/" },
    { id: "slides", label: "Slides", name: "Slides", group: "everyday", href: hd("https://docs.google.com/presentation/") },
    { id: "contacts", label: "Contacts", name: "Contacts", group: "everyday", href: hd("https://contacts.google.com/") },
    { id: "tasks", label: "Tasks", name: "Tasks", group: "everyday", href: hd("https://tasks.google.com/") },
    { id: "sites", label: "Sites", name: "Sites", group: "more", href: "https://sites.google.com/a/" + DOMAIN },
    { id: "groups", label: "Groups", name: "Groups", group: "more", href: hd("https://groups.google.com/a/" + DOMAIN) },
    { id: "admin", label: "Admin", name: "Admin", group: "more", href: "https://admin.google.com/" + DOMAIN },
    { id: "drawings", label: "Drawings", name: "Drawings", group: "more", href: hd("https://docs.google.com/drawings/") },
    { id: "voice", label: "Voice", name: "Voice", group: "more", href: hd("https://voice.google.com/") },
    { id: "classroom", label: "Classroom", name: "Classroom", group: "more", href: "https://classroom.google.com/a/" + DOMAIN },
    { id: "youtube", label: "YouTube", name: "YouTube", group: "more", href: "https://www.youtube.com/" },
    { id: "photos", label: "Photos", name: "Photos", group: "more", href: hd("https://photos.google.com/") },
    { id: "maps", label: "Maps", name: "Maps", group: "more", href: "https://www.google.com/maps" },
    { id: "earth", label: "Earth", name: "Earth", group: "more", href: "https://earth.google.com/web/" },
    { id: "translate", label: "Translate", name: "Translate", group: "more", href: "https://translate.google.com/" },
    { id: "gemini", label: "Gemini", name: "Gemini", group: "more", href: hd("https://gemini.google.com/") },
    { id: "analytics", label: "Analytics", name: "Analytics", group: "more", href: hd("https://analytics.google.com/") },
    { id: "looker", label: "Looker", name: "Looker Studio", group: "more", href: hd("https://lookerstudio.google.com/") },
    { id: "search", label: "Search", name: "Search Console", group: "more", href: hd("https://search.google.com/search-console") },
    { id: "business", label: "Business", name: "Business Profile", group: "more", href: hd("https://business.google.com/") },
    { id: "mymaps", label: "My Maps", name: "My Maps", group: "more", href: hd("https://www.google.com/maps/d/") },
    { id: "script", label: "Script", name: "Apps Script", group: "more", href: "https://script.google.com/a/" + DOMAIN },
    { id: "notebook", label: "Notebook", name: "NotebookLM", group: "more", href: hd("https://notebooklm.google.com/") },
    { id: "vids", label: "Vids", name: "Google Vids", group: "more", href: hd("https://docs.google.com/videos/") }
  ];

  function add(a, b) { return { x: a.x + b.x, y: a.y + b.y, z: a.z + b.z }; }
  function sub(a, b) { return { x: a.x - b.x, y: a.y - b.y, z: a.z - b.z }; }
  function mul(a, s) { return { x: a.x * s, y: a.y * s, z: a.z * s }; }
  function dot(a, b) { return a.x * b.x + a.y * b.y + a.z * b.z; }
  function cross(a, b) {
    return { x: a.y * b.z - a.z * b.y, y: a.z * b.x - a.x * b.z, z: a.x * b.y - a.y * b.x };
  }
  function len(a) { return Math.hypot(a.x, a.y, a.z); }
  function norm(a) {
    var l = len(a) || 1;
    return { x: a.x / l, y: a.y / l, z: a.z / l };
  }
  function lerp(a, b, t) { return add(mul(a, 1 - t), mul(b, t)); }
  function average(pts) {
    var s = { x: 0, y: 0, z: 0 };
    for (var i = 0; i < pts.length; i++) s = add(s, pts[i]);
    return mul(s, 1 / pts.length);
  }
  function ortho(n) {
    var a = Math.abs(n.y) < 0.9 ? { x: 0, y: 1, z: 0 } : { x: 1, y: 0, z: 0 };
    return norm(cross(a, n));
  }

  function matVec(m, v) {
    return {
      x: m[0] * v.x + m[1] * v.y + m[2] * v.z,
      y: m[3] * v.x + m[4] * v.y + m[5] * v.z,
      z: m[6] * v.x + m[7] * v.y + m[8] * v.z
    };
  }
  function mulMat(a, b) {
    var o = new Array(9);
    for (var r = 0; r < 3; r++) {
      for (var c = 0; c < 3; c++) {
        o[r * 3 + c] = a[r * 3] * b[c] + a[r * 3 + 1] * b[3 + c] + a[r * 3 + 2] * b[6 + c];
      }
    }
    return o;
  }
  function basis(u, v, n) {
    return [u.x, v.x, n.x, u.y, v.y, n.y, u.z, v.z, n.z];
  }
  function rotAround(axis, angle) {
    var u = norm(axis);
    var c = Math.cos(angle);
    var s = Math.sin(angle);
    var t = 1 - c;
    var x = u.x, y = u.y, z = u.z;
    return [
      t * x * x + c, t * x * y - s * z, t * x * z + s * y,
      t * x * y + s * z, t * y * y + c, t * y * z - s * x,
      t * x * z - s * y, t * y * z + s * x, t * z * z + c
    ];
  }
  function rotX(a) {
    var c = Math.cos(a), s = Math.sin(a);
    return [1, 0, 0, 0, c, -s, 0, s, c];
  }
  function rotY(a) {
    var c = Math.cos(a), s = Math.sin(a);
    return [c, 0, s, 0, 1, 0, -s, 0, c];
  }
  function rotationFromTo(a, b) {
    var u = norm(a), v = norm(b);
    var d = Math.max(-1, Math.min(1, dot(u, v)));
    if (d > 0.999999) return [1, 0, 0, 0, 1, 0, 0, 0, 1];
    if (d < -0.999999) return rotAround(ortho(u), Math.PI);
    return rotAround(cross(u, v), Math.acos(d));
  }
  function cssMatrix(m, t) {
    function e(n) { return n.toFixed(4); }
    return "matrix3d(" +
      e(m[0]) + "," + e(m[3]) + "," + e(m[6]) + ",0," +
      e(m[1]) + "," + e(m[4]) + "," + e(m[7]) + ",0," +
      e(m[2]) + "," + e(m[5]) + "," + e(m[8]) + ",0," +
      e(t.x) + "," + e(t.y) + "," + e(t.z) + ",1)";
  }
  function orthonormalize(m) {
    var x = norm({ x: m[0], y: m[3], z: m[6] });
    var y = { x: m[1], y: m[4], z: m[7] };
    y = norm(sub(y, mul(x, dot(x, y))));
    var z = cross(x, y);
    return basis(x, y, z);
  }

  function icosahedron() {
    var p = (1 + Math.sqrt(5)) / 2;
    var verts = [];
    var s1, s2;
    for (s1 = -1; s1 <= 1; s1 += 2) {
      for (s2 = -1; s2 <= 1; s2 += 2) {
        verts.push({ x: 0, y: s1, z: s2 * p });
        verts.push({ x: s1, y: s2 * p, z: 0 });
        verts.push({ x: s2 * p, y: 0, z: s1 });
      }
    }
    var min = Infinity;
    var i, j;
    for (i = 0; i < verts.length; i++) {
      for (j = i + 1; j < verts.length; j++) min = Math.min(min, len(sub(verts[i], verts[j])));
    }
    var adj = verts.map(function () { return []; });
    for (i = 0; i < verts.length; i++) {
      for (j = i + 1; j < verts.length; j++) {
        if (len(sub(verts[i], verts[j])) <= min * 1.01) {
          adj[i].push(j);
          adj[j].push(i);
        }
      }
    }
    var sorted = adj.map(function (neigh, idx) {
      var n = norm(verts[idx]);
      var t = ortho(n);
      var b = cross(n, t);
      return neigh.slice().sort(function (a, c) {
        var da = sub(verts[a], verts[idx]);
        var dc = sub(verts[c], verts[idx]);
        return Math.atan2(dot(da, b), dot(da, t)) - Math.atan2(dot(dc, b), dot(dc, t));
      });
    });
    return { verts: verts, sorted: sorted, edge: min };
  }

  function walkFaces(sorted, dir) {
    var used = {};
    var faces = [];
    var i, j, prev, curr, poly, guard, neigh, idx, next;
    for (i = 0; i < sorted.length; i++) {
      for (j = 0; j < sorted[i].length; j++) {
        var start = sorted[i][j];
        if (used[i + ">" + start]) continue;
        poly = [i];
        prev = i;
        curr = start;
        guard = 0;
        while (curr !== i && guard++ < 14) {
          used[prev + ">" + curr] = 1;
          poly.push(curr);
          neigh = sorted[curr];
          idx = neigh.indexOf(prev);
          next = neigh[(idx + dir + neigh.length) % neigh.length];
          prev = curr;
          curr = next;
        }
        used[prev + ">" + i] = 1;
        if (curr === i && poly.length >= 3) faces.push(poly);
      }
    }
    return faces;
  }

  function newell(pts) {
    var n = { x: 0, y: 0, z: 0 };
    var i, a, b;
    for (i = 0; i < pts.length; i++) {
      a = pts[i];
      b = pts[(i + 1) % pts.length];
      n.x += (a.y - b.y) * (a.z + b.z);
      n.y += (a.z - b.z) * (a.x + b.x);
      n.z += (a.x - b.x) * (a.y + b.y);
    }
    return n;
  }

  function trianglesOf(ico) {
    var dir, faces, outward, trial, pts, c, n, k;
    for (dir = -1; dir <= 1; dir += 2) {
      faces = walkFaces(ico.sorted, dir);
      if (faces.length !== 20) continue;
      if (!faces.every(function (f) { return f.length === 3; })) continue;
      outward = 0;
      for (k = 0; k < faces.length; k++) {
        pts = faces[k].map(function (ix) { return ico.verts[ix]; });
        c = average(pts);
        n = newell(pts);
        if (dot(n, c) > 0) outward++;
      }
      if (outward === 20) return faces;
      if (outward === 0) {
        return faces.map(function (f) { return f.slice().reverse(); });
      }
    }
    throw new Error("icosahedron faces not found");
  }

  function pentEdge(ico, t) {
    var i = 0;
    var a = ico.verts[i];
    var n0 = ico.verts[ico.sorted[i][0]];
    var n1 = ico.verts[ico.sorted[i][1]];
    return len(sub(lerp(a, n0, t), lerp(a, n1, t)));
  }

  function solveT(ico) {
    var lo = 0.05, hi = 0.45, mid, k;
    for (k = 0; k < 48; k++) {
      mid = (lo + hi) / 2;
      if (pentEdge(ico, mid) > (1 - 2 * mid) * ico.edge) hi = mid;
      else lo = mid;
    }
    return (lo + hi) / 2;
  }

  function clipFor(pts, center, normal) {
    var n = norm(normal);
    var u = ortho(n);
    var v = cross(n, u);
    var flat = pts.map(function (p) {
      var d = sub(p, center);
      return { x: dot(d, u), y: dot(d, v), p: p };
    });
    flat.sort(function (a, b) { return Math.atan2(a.y, a.x) - Math.atan2(b.y, b.x); });
    var r = 0;
    var i;
    for (i = 0; i < flat.length; i++) r = Math.max(r, Math.hypot(flat[i].x, flat[i].y));
    return {
      pts: flat.map(function (q) { return q.p; }),
      flat: flat.map(function (q) { return { x: q.x, y: q.y }; }),
      u: u,
      v: v,
      n: n,
      center: center,
      unitR: r
    };
  }

  function buildModel() {
    var ico = icosahedron();
    if (ico.verts.length !== 12) throw new Error("expected 12 icosahedron vertices");
    if (ico.sorted.some(function (n) { return n.length !== 5; })) throw new Error("icosahedron degree");
    var tris = trianglesOf(ico);
    var t = solveT(ico);
    var faces = [];
    var i, neigh, poly, tri, A, B, C;

    for (i = 0; i < ico.verts.length; i++) {
      neigh = ico.sorted[i];
      poly = neigh.map(function (j) { return lerp(ico.verts[i], ico.verts[j], t); });
      faces.push(poly);
    }
    for (i = 0; i < tris.length; i++) {
      tri = tris[i];
      A = ico.verts[tri[0]];
      B = ico.verts[tri[1]];
      C = ico.verts[tri[2]];
      faces.push([
        lerp(A, B, t),
        lerp(B, A, t),
        lerp(B, C, t),
        lerp(C, B, t),
        lerp(C, A, t),
        lerp(A, C, t)
      ]);
    }

    var cr = 0;
    faces.forEach(function (pts) {
      pts.forEach(function (p) { cr = Math.max(cr, len(p)); });
    });
    var built = faces.map(function (pts) {
      var scaled = pts.map(function (p) { return mul(p, 1 / cr); });
      var center = average(scaled);
      var shaped = clipFor(scaled, center, center);
      shaped.sides = shaped.pts.length;
      return shaped;
    });

    var pent = built.filter(function (f) { return f.sides === 5; });
    var hex = built.filter(function (f) { return f.sides === 6; });
    if (pent.length !== 12 || hex.length !== 20) {
      throw new Error("face count " + pent.length + " pent / " + hex.length + " hex");
    }

    var minE = Infinity, maxE = 0;
    built.forEach(function (f) {
      var k, e, skip, radii = [], mean = 0;
      for (k = 0; k < f.pts.length; k++) {
        e = len(sub(f.pts[k], f.pts[(k + 1) % f.pts.length]));
        minE = Math.min(minE, e);
        maxE = Math.max(maxE, e);
        skip = len(sub(f.pts[k], f.pts[(k + 2) % f.pts.length]));
        if (skip <= e * 1.05) throw new Error("face is not a simple polygon");
        radii.push(len(sub(f.pts[k], f.center)));
      }
      radii.forEach(function (r) { mean += r; });
      mean /= radii.length;
      radii.forEach(function (r) {
        if (Math.abs(r - mean) / mean > 0.02) throw new Error("face not regular");
      });
      if (dot(f.n, f.center) <= 0) throw new Error("normal faces inward");
    });

    function near(a, b) { return len(sub(a, b)) < 1e-6; }
    function adjacent(a, b) {
      var n = 0, ia, ib;
      for (ia = 0; ia < a.pts.length; ia++) {
        for (ib = 0; ib < b.pts.length; ib++) if (near(a.pts[ia], b.pts[ib])) n++;
      }
      return n >= 2;
    }
    function around(face) {
      var list = built.filter(function (g) { return g !== face && adjacent(face, g); });
      var tng = ortho(face.n);
      var b = cross(face.n, tng);
      list.sort(function (a, c) {
        var da = sub(a.center, face.center);
        var dc = sub(c.center, face.center);
        return Math.atan2(dot(da, b), dot(da, tng)) - Math.atan2(dot(dc, b), dot(dc, tng));
      });
      return list;
    }

    var start = pent.slice().sort(function (a, b) {
      return b.n.z - a.n.z || b.n.x - a.n.x;
    })[0];
    var seen = new Set();
    var queue = [start];
    var order = [];
    seen.add(start);
    while (queue.length) {
      var f = queue.shift();
      order.push(f);
      around(f).forEach(function (g) {
        if (!seen.has(g)) {
          seen.add(g);
          queue.push(g);
        }
      });
    }
    if (order.length !== SERVICES.length) throw new Error("assignment " + order.length);
    order.forEach(function (f, ix) { f.service = SERVICES[ix]; });

    return {
      faces: order,
      t: t,
      edgeRatio: maxE / minE,
      start: start
    };
  }

  if (typeof document === "undefined") {
    var model = buildModel();
    var front = matVec(rotY(Math.PI / 2), { x: 0, y: 0, z: 1 });
    if (Math.abs(front.x - 1) > 1e-9 || Math.abs(front.z) > 1e-9) {
      throw new Error("rotY check failed");
    }
    var up = matVec(rotX(Math.PI / 2), { x: 0, y: 0, z: 1 });
    if (Math.abs(up.y + 1) > 1e-9) throw new Error("rotX check failed");
    var aimed = matVec(rotationFromTo({ x: 0.2, y: -0.4, z: 0.5 }, { x: 0, y: 1, z: 0 }), norm({ x: 0.2, y: -0.4, z: 0.5 }));
    if (Math.abs(aimed.y - 1) > 1e-9) throw new Error("rotationFromTo failed");
    if (model.edgeRatio > 1.01) throw new Error("edges uneven " + model.edgeRatio);
    model.faces.forEach(function (f) {
      var expect = Math.PI * (f.sides - 2) / f.sides;
      var i, a, b, c, ux, uy, vx, vy, ang, e0, e1;
      for (i = 0; i < f.sides; i++) {
        a = f.flat[(i + f.sides - 1) % f.sides];
        b = f.flat[i];
        c = f.flat[(i + 1) % f.sides];
        ux = a.x - b.x; uy = a.y - b.y;
        vx = c.x - b.x; vy = c.y - b.y;
        ang = Math.atan2(Math.abs(ux * vy - uy * vx), ux * vx + uy * vy);
        if (Math.abs(ang - expect) > 0.04) throw new Error("bad corner on " + f.sides + "-gon " + ang);
        e0 = Math.hypot(b.x - a.x, b.y - a.y);
        e1 = Math.hypot(c.x - b.x, c.y - b.y);
        if (Math.abs(e0 - e1) / e0 > 0.02) throw new Error("uneven 2D edge");
      }
    });
    var fs = require("fs");
    var ids = {};
    model.faces.forEach(function (f) {
      if (!fs.existsSync("img/google/" + f.service.id + ".png")) throw new Error("no icon " + f.service.id);
      if (ids[f.service.id]) throw new Error("dup " + f.service.id);
      ids[f.service.id] = 1;
      console.log([f.service.name, f.sides === 5 ? "pentagon" : "hexagon", f.service.href].join("\t"));
    });
    console.log("OK faces=" + model.faces.length + " t=" + model.t.toFixed(5) + " edgeRatio=" + model.edgeRatio.toFixed(5));
    return;
  }

  function icon(id) {
    return '<img class="brand-icon" src="/img/google/' + id + '.png" alt="" width="64" height="64">';
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var stage = document.getElementById("board-stage");
  var ball = document.getElementById("board-ball");
  var readout = document.getElementById("board-readout");
  var list = document.getElementById("service-list");
  var model = null;
  var R = [1, 0, 0, 0, 1, 0, 0, 0, 1];
  var builtRadius = -1;
  var dragging = false;
  var autoSpin = false;
  var spinTimer = 0;
  var velYaw = 0;
  var velPitch = 0;
  var blockClick = false;
  var moved = 0;
  var active = null;
  var running = false;
  var lastTick = 0;

  function renderList() {
    var group = "";
    SERVICES.forEach(function (s) {
      if (s.group !== group) {
        var h = document.createElement("h3");
        h.textContent = s.group === "everyday" ? "Everyday" : "More tools";
        list.appendChild(h);
        group = s.group;
      }
      var a = document.createElement("a");
      a.href = s.href;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.innerHTML = icon(s.id) + "<span>" + esc(s.name) + "</span>";
      list.appendChild(a);
    });
  }

  function layoutRadius() {
    var size = Math.min(stage.clientWidth, stage.clientHeight);
    return Math.max(96, size * 0.36);
  }

  function facePoints(f, w) {
    return f.flat.map(function (q) {
      var x = w / 2 + (q.x / f.unitR) * (w / 2);
      var y = w / 2 + (q.y / f.unitR) * (w / 2);
      return x.toFixed(2) + "," + y.toFixed(2);
    }).join(" ");
  }

  function buildDom(radius) {
    ball.textContent = "";
    model.faces.forEach(function (f) {
      var w = 2 * f.unitR * radius;
      var a = document.createElement("a");
      var pts = facePoints(f, w);
      var fill = f.sides === 5 ? "#111111" : "#f7f5ef";
      var seam = Math.max(2.5, w * 0.055);
      a.className = "face " + (f.sides === 5 ? "pent" : "hex");
      a.href = f.service.href;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.dataset.name = f.service.name;
      a.setAttribute("aria-label", f.service.name);
      a.style.width = w + "px";
      a.style.height = w + "px";
      a.style.marginLeft = (-w / 2) + "px";
      a.style.marginTop = (-w / 2) + "px";
      a.innerHTML =
        '<svg class="panel-svg" viewBox="0 0 ' + w.toFixed(2) + " " + w.toFixed(2) + '" aria-hidden="true" focusable="false">' +
        '<polygon class="skin" points="' + pts + '" fill="' + fill + '" stroke="#eac300" stroke-width="' + seam.toFixed(2) + '" stroke-linejoin="round"/>' +
        '<polygon class="shade" points="' + pts + '" fill="#000"/>' +
        "</svg>" +
        '<span class="label">' + icon(f.service.id) + '<span class="name">' + esc(f.service.label) + "</span></span>";
      var name = a.querySelector(".name");
      var long = f.service.label.length >= 9;
      name.style.fontSize = Math.max(11, w * (long ? 0.082 : 0.098)) + "px";
      var mark = a.querySelector(".label img");
      var s = Math.max(22, w * 0.30);
      mark.style.width = s + "px";
      mark.style.height = s + "px";
      f.el = a;
      f.labelEl = a.querySelector(".label");
      f.skin = a.querySelector(".skin");
      f.shadeEl = a.querySelector(".shade");
      f.pixelCenter = mul(f.center, radius);
      ball.appendChild(a);
    });
    builtRadius = radius;
    stage.style.perspective = (radius * 4.6) + "px";
  }

  function paint() {
    R = orthonormalize(R);
    ball.style.transform = cssMatrix(R, { x: 0, y: 0, z: 0 });
    model.faces.forEach(function (f) {
      var worldN = matVec(R, f.n);
      var parent = basis(f.u, f.v, f.n);
      f.el.style.transform = cssMatrix(parent, f.pixelCenter);
      var front = Math.max(0, worldN.z);
      f.shadeEl.style.opacity = (0.5 * (1 - front)).toFixed(3);
      f.skin.style.pointerEvents = worldN.z > 0.18 ? "auto" : "none";
      var uw = matVec(R, f.u);
      var vw = matVec(R, f.v);
      var down = { x: 0, y: 1, z: 0 };
      var du = dot(down, uw);
      var dv = dot(down, vw);
      if (Math.hypot(du, dv) > 0.2) {
        var theta = -Math.atan2(du, dv);
        f.labelEl.style.transform = "translate(-50%, -50%) rotate(" + theta.toFixed(4) + "rad)";
      }
    });
  }

  function kick() {
    if (running) return;
    running = true;
    lastTick = performance.now();
    requestAnimationFrame(tick);
  }
  function tick(now) {
    var dt = Math.min(34, now - lastTick);
    lastTick = now;
    var moving = dragging || Math.abs(velYaw) + Math.abs(velPitch) > 0.0004 || autoSpin;
    if (!dragging && (Math.abs(velYaw) + Math.abs(velPitch) > 0.0004)) {
      R = mulMat(rotY(velYaw), mulMat(rotX(velPitch), R));
      var decay = Math.pow(0.9, dt / 16.7);
      velYaw *= decay;
      velPitch *= decay;
      if (Math.abs(velYaw) + Math.abs(velPitch) < 0.0004) {
        velYaw = 0;
        velPitch = 0;
      }
    }
    if (autoSpin && !dragging) R = mulMat(rotY(0.00028 * dt), R);
    paint();
    if (moving) requestAnimationFrame(tick);
    else running = false;
  }

  function queueSpin() {
    autoSpin = false;
    if (reduce) return;
    clearTimeout(spinTimer);
    spinTimer = setTimeout(function () {
      autoSpin = true;
      kick();
    }, 3200);
  }

  function ensure() {
    var radius = layoutRadius();
    if (!model) return;
    if (Math.abs(radius - builtRadius) > 0.75) buildDom(radius);
    paint();
  }

  renderList();
  try {
    model = buildModel();
    R = rotationFromTo(model.start.n, { x: 0, y: 0, z: 1 });
    R = mulMat(rotY(0.34), mulMat(rotX(-0.46), R));
    ensure();
    document.documentElement.dataset.ball = "ready";
    if (!reduce) {
      spinTimer = setTimeout(function () {
        autoSpin = true;
        kick();
      }, 4000);
    }
  } catch (err) {
    readout.textContent = "The ball could not be drawn. Use the list below.";
    if (typeof console !== "undefined") console.error(err);
  }

  window.addEventListener("resize", function () {
    if (!model) return;
    ensure();
    kick();
  });

  stage.addEventListener("pointerdown", function (e) {
    if (e.button !== undefined && e.button !== 0) return;
    dragging = true;
    moved = 0;
    velYaw = 0;
    velPitch = 0;
    autoSpin = false;
    clearTimeout(spinTimer);
    active = { id: e.pointerId, x: e.clientX, y: e.clientY };
    stage.classList.add("is-dragging");
    kick();
  });
  window.addEventListener("pointermove", function (e) {
    if (!active || e.pointerId !== active.id) return;
    var dx = e.clientX - active.x;
    var dy = e.clientY - active.y;
    active.x = e.clientX;
    active.y = e.clientY;
    moved += Math.abs(dx) + Math.abs(dy);
    var k = 0.0072;
    velYaw = dx * k;
    velPitch = -dy * k;
    R = mulMat(rotY(velYaw), mulMat(rotX(velPitch), R));
    kick();
  });
  function endDrag(e) {
    if (!active || (e && e.pointerId !== active.id)) return;
    active = null;
    dragging = false;
    stage.classList.remove("is-dragging");
    if (moved > 8) {
      blockClick = true;
      setTimeout(function () { blockClick = false; }, 350);
    } else if (reduce) {
      velYaw = 0;
      velPitch = 0;
    }
    queueSpin();
    kick();
  }
  window.addEventListener("pointerup", endDrag);
  window.addEventListener("pointercancel", endDrag);

  ball.addEventListener("click", function (e) {
    if (!blockClick) return;
    e.preventDefault();
    e.stopPropagation();
    blockClick = false;
  }, true);
  ball.addEventListener("dragstart", function (e) { e.preventDefault(); });
  ball.addEventListener("pointerover", function (e) {
    var a = e.target.closest ? e.target.closest("a.face") : null;
    if (a) readout.textContent = a.dataset.name;
  });
  ball.addEventListener("pointerleave", function () {
    readout.textContent = "Cecil Soccer League";
  });

  stage.addEventListener("keydown", function (e) {
    var step = 0.16;
    var handled = true;
    if (e.key === "ArrowLeft") R = mulMat(rotY(-step), R);
    else if (e.key === "ArrowRight") R = mulMat(rotY(step), R);
    else if (e.key === "ArrowUp") R = mulMat(rotX(step), R);
    else if (e.key === "ArrowDown") R = mulMat(rotX(-step), R);
    else handled = false;
    if (!handled) return;
    e.preventDefault();
    velYaw = 0;
    velPitch = 0;
    queueSpin();
    kick();
  });
})();
