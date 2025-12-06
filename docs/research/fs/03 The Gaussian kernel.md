# 3. The Gaussian kernel

> Of all things, man is the measure.
> 
> — Protagoras the Sophist (480-411 B.C.)

## 3.1 The Gaussian kernel

The Gaussian (better Gaußian) kernel is named after Carl Friedrich Gauß (1777-1855), a brilliant German mathematician. This chapter discusses many of the attractive and special properties of the Gaussian kernel.

```mathematica
<< FrontEndVision`FEV`; Show@Import@"Gauss10DM.gif"D, ImageSize -> 280D;
```

**Figure 3.1** The Gaussian kernel is apparent on every German banknote of DM 10,- where it is depicted next to its famous inventor when he was 55 years old. The new Euro replaces these banknotes. See also: http://scienceworld.wolfram.com/biography/Gauss.html.

The Gaussian kernel is defined in 1-D, 2D and N-D respectively as:

$$G_{1D}(x; \sigma) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{x^2}{2\sigma^2}}$$

$$G_{2D}(x, y; \sigma) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}$$

$$G_{ND}(\vec{x}; \sigma) = \frac{1}{(\sqrt{2\pi}\sigma)^N} e^{-\frac{|\vec{x}|^2}{2\sigma^2}}$$

The $\sigma$ determines the width of the Gaussian kernel. In statistics, when we consider the Gaussian probability density function it is called the standard deviation, and the square of it, $\sigma^2$, the variance. In the rest of this book, when we consider the Gaussian as an aperture function of some observation, we will refer to $\sigma$ as the inner scale or shortly scale.

In the whole of this book the scale can only take positive values, $\sigma > 0$. In the process of observation $\sigma$ can never become zero. For, this would imply making an observation through an infinitesimally small aperture, which is impossible. The factor of 2 in the exponent is a matter of convention, because we then have a 'cleaner' formula for the diffusion equation, as we will see later on. The semicolon between the spatial and scale parameters is conventionally put there to make the difference between these parameters explicit.

The scale-dimension is not just another spatial dimension, as we will thoroughly discuss in the remainder of this book.

The half width at half maximum ($\sigma = 2\sqrt{2 \ln 2}$) is often used to approximate $\sigma$, but it is somewhat larger:

```mathematica
Unprotect@gaussD;
gauss@x_, s_D := 1/(s Sqrt[2 Pi]) Exp[-x^2/(2 s^2)];
Solve[gauss[x, s]/gauss[0, s] == 1/2, x]
```

Output:
```
{{x -> -s Sqrt[2 Log[2]]}, {x -> s Sqrt[2 Log[2]]}}
```

```mathematica
% // N
```

Output:
```
{{x -> -1.17741 s}, {x -> 1.17741 s}}
```

## 3.2 Normalization

The term $\frac{1}{\sqrt{2\pi}\sigma}$ in front of the one-dimensional Gaussian kernel is the normalization constant. It comes from the fact that the integral over the exponential function is not unity: $\int_{-\infty}^{\infty} e^{-x^2/(2\sigma^2)} dx = \sqrt{2\pi}\sigma$. With the normalization constant this Gaussian kernel is a normalized kernel, i.e. its integral over its full domain is unity for every $\sigma$.

This means that increasing the $\sigma$ of the kernel reduces the amplitude substantially. Let us look at the graphs of the normalized kernels for $\sigma = 0.3$, $\sigma = 1$ and $\sigma = 2$ plotted on the same axes:

```mathematica
Unprotect@gaussD; 
gauss@x_, s_D := 1/(s Sqrt[2 Pi]) Exp[-x^2/(2 s^2)];
Block[{$DisplayFunction = Identity}, 
  {p1, p2, p3} = Plot[gauss[x, s = #], {x, -5, 5}, PlotRange -> {0, 1.4}] & /@ {.3, 1, 2}
];
Show[GraphicsArray[{p1, p2, p3}], ImageSize -> 400];
```

**Figure 3.2** The Gaussian function at scales $\sigma = 0.3$, $\sigma = 1$ and $\sigma = 2$. The kernel is normalized, so the total area under the curve is always unity.

The normalization ensures that the average graylevel of the image remains the same when we blur the image with this kernel. This is known as average grey level invariance.

## 3.3 Cascade property, selfsimilarity

The shape of the kernel remains the same, irrespective of the $\sigma$. When we convolve two Gaussian kernels we get a new wider Gaussian with a variance $\sigma^2$ which is the sum of the variances of the constituting Gaussians: $g_{new}(\vec{x}; \sigma_1^2 + \sigma_2^2) = g_1(\vec{x}; \sigma_1^2) * g_2(\vec{x}; \sigma_2^2)$.

```mathematica
s = .; 
Simplify[Integrate[gauss[a, s1] gauss[a - x, s2], {a, -Infinity, Infinity}], 
  {s1 > 0, s2 > 0}]
```

Output:
$$\frac{e^{-\frac{x^2}{2(\sigma_1^2 + \sigma_2^2)}}}{\sqrt{2\pi}\sqrt{\sigma_1^2 + \sigma_2^2}}$$

This phenomenon, i.e. that a new function emerges that is similar to the constituting functions, is called self-similarity.

The Gaussian is a self-similar function. Convolution with a Gaussian is a linear operation, so a convolution with a Gaussian kernel followed by a convolution with again a Gaussian kernel is equivalent to convolution with the broader kernel. Note that the squares of $\sigma$ add, not the $\sigma$'s themselves. Of course we can concatenate as many blurring steps as we want to create a larger blurring step. With analogy to a cascade of waterfalls spanning the same height as the total waterfall, this phenomenon is also known as the cascade smoothing property.

Famous examples of self-similar functions are fractals. This shows the famous Mandelbrot fractal:

```mathematica
cMandelbrot = Compile[{{c, _Complex}}, 
  -Length[FixedPointList[#^2 + c &, c, 50, SameTest -> (Abs[#2] > 2.0 &)]]];
ListDensityPlot[-Table[cMandelbrot[a + b I], {b, -1.1, 1.1, 0.0114}, 
  {a, -2.0, 0.5, 0.0142}], Mesh -> False, AspectRatio -> Automatic, 
  Frame -> False, ColorFunction -> Hue, ImageSize -> 170];
```

**Figure 3.3** The Mandelbrot fractal is a famous example of a self-similar function. Source: www.mathforum.org. See also mathworld.wolfram.com/MandelbrotSet.html.

## 3.4 The scale parameter

In order to avoid the summing of squares, one often uses the following parametrization: $2\sigma^2 \rightarrow t$, so the Gaussian kernel get a particular short form. In N dimensions:

$$G_{ND}(\vec{x}, t) = \frac{1}{(\pi t)^{N/2}} e^{-\frac{x^2}{t}}$$

It is this $t$ that emerges in the diffusion equation $\frac{\partial L}{\partial t} = \frac{\partial^2 L}{\partial x^2} + \frac{\partial^2 L}{\partial y^2} + \frac{\partial^2 L}{\partial z^2}$. It is often referred to as 'scale' (like in: differentiation to scale, $\frac{\partial L}{\partial t}$), but a better name is variance.

To make the self-similarity of the Gaussian kernel explicit, we can introduce a new dimensionless spatial parameter, $\tilde{x} = \frac{x}{\sigma\sqrt{2}}$. We say that we have reparametrized the x-axis.

Now the Gaussian kernel becomes: $g_n(\tilde{x}; \sigma) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\tilde{x}^2}$, or $g_n(\tilde{x}; t) = \frac{1}{(\pi t)^{N/2}} e^{-\tilde{x}^2}$. In other words: if we walk along the spatial axis in footsteps expressed in scale-units ($\sigma$'s), all kernels are of equal size or 'width' (but due to the normalization constraint not necessarily of the same amplitude). We now have a 'natural' size of footstep to walk over the spatial coordinate: a unit step in x is now $\sigma\sqrt{2}$, so in more blurred images we make bigger steps.

We call this basic Gaussian kernel the natural Gaussian kernel $g_n(\tilde{x}; \sigma)$. The new coordinate $\tilde{x} = \frac{x}{\sigma\sqrt{2}}$ is called the natural coordinate. It eliminates the scale factor $\sigma$ from the spatial coordinates, i.e. it makes the Gaussian kernels similar, despite their different inner scales. We will encounter natural coordinates many times hereafter.

The spatial extent of the Gaussian kernel ranges from $-\infty$ to $+\infty$, but in practice it has negligible values for x larger then a few (say 5) $\sigma$. The numerical value at $x=5\sigma$, and the area under the curve from $x=5\sigma$ to infinity (recall that the total area is 1):

```mathematica
gauss[5, 1] // N
Integrate[gauss[x, 1], {x, 5, Infinity}] // N
```

Output:
```
1.48672 × 10^-6
2.86652 × 10^-7
```

The larger we make the standard deviation $\sigma$, the more the image gets blurred. In the limit to infinity, the image becomes homogenous in intensity. The final intensity is the average intensity of the image. This is true for an image with infinite extent, which in practice will never occur, of course. The boundary has to be taken into account. Actually, one can take many choices what to do at the boundary, it is a matter of consensus. Boundaries are discussed in detail in chapter 5, where practical issues of computer implementation are discussed.

## 3.5 Relation to generalized functions

The Gaussian kernel is the physical equivalent of the mathematical point. It is not strictly local, like the mathematical point, but semi-local. It has a Gaussian weighted extent, indicated by its inner scale $\sigma$.

Because scale-space theory is revolving around the Gaussian function and its derivatives as a physical differential operator (in more detail explained in the next chapter), we will focus here on some mathematical notions that are directly related, i.e. the mathematical notions underlying sampling of values from functions and their derivatives at selected points (i.e. that is why it is referred to as sampling). The mathematical functions involved are the generalized functions, i.e. the Delta-Dirac function, the Heaviside function and the error function. In the next section we study these functions in detail.

When we take the limit as the inner scale goes down to zero (remember that $\sigma$ can only take positive values for a physically realistic system), we get the mathematical delta function, or Dirac delta function, $\delta(x)$. This function is everywhere zero except in $x = 0$, where it has infinite amplitude and zero width, its area is unity.

$$\lim_{\sigma \to 0} \left(\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{x^2}{2\sigma^2}}\right) = \delta(x)$$

$\delta(x)$ is called the sampling function in mathematics, because the Dirac delta function adequately samples just one point out of a function when integrated. It is assumed that $f(x)$ is continuous at $x = a$:

```mathematica
Integrate[DiracDelta[x - a] f[x], {x, -Infinity, Infinity}]
```

Output:
```
f[a]
```

The sampling property of derivatives of the Dirac delta function is shown below:

```mathematica
Integrate[D[DiracDelta[x], {x, 2}] f[x], {x, -Infinity, Infinity}]
```

Output:
```
f''[0]
```

The delta function was originally proposed by the eccentric Victorian mathematician Oliver Heaviside (1880-1925, see also [Pickover1998]). Story goes that mathematicians called this function a "monstrosity", but it did work! Around 1950 physicist Paul Dirac (1902-1984) gave it new light. Mathematician Laurent Schwartz (1915-) proved it in 1951 with his famous "theory of distributions" (we discuss this theory in chapter 8). And today it's called "the Dirac delta function".

The integral of the Gaussian kernel from $-\infty$ to x is a famous function as well. It is the error function, or cumulative Gaussian function, and is defined as:

```mathematica
s = .; 
err[x_, s_] = Integrate[1/(s Sqrt[2 Pi]) Exp[-y^2/(2 s^2)], {y, x, Infinity}]
```

Output:
$$\frac{1}{2}\text{Erf}\left(\frac{x}{\sqrt{2}\sigma}\right)$$

The y in the integral above is just a dummy integration variable, and is integrated out. The Mathematica error function is `Erf[x]`.

In our integral of the Gaussian function we need to do the reparametrization $x \rightarrow \frac{x}{\sigma\sqrt{2}}$. Again we recognize the natural coordinates. The factor $\frac{1}{2}$ is due to the fact that integration starts halfway, in $x = 0$.

```mathematica
s = 1.; 
Plot[1/2 Erf[x/(s Sqrt[2])], {x, -4, 4}, AspectRatio -> .3, 
  AxesLabel -> {"x", "Erf[x]"}, ImageSize -> 200];
```

**Figure 3.4** The error function `Erf[x]` is the cumulative Gaussian function.

When the inner scale $\sigma$ of the error function goes to zero, we get in the limiting case the so-called Heavyside function or unitstep function. The derivative of the Heavyside function is the Delta-Dirac function, just as the derivative of the error function of the Gaussian kernel.

```mathematica
s = .1; 
Plot[1/2 Erf[x/(s Sqrt[2])], {x, -4, 4}, AspectRatio -> .3, 
  AxesLabel -> {"x", "Erf[x]"}, ImageSize -> 270];
```

**Figure 3.5** For decreasing $\sigma$ the Error function begins to look like a step function. The Error function is the Gaussian blurred step-edge.

```mathematica
Plot[UnitStep[x], {x, -4, 4}, DisplayFunction -> $DisplayFunction, 
  AspectRatio -> .3, AxesLabel -> {"x", "Heavyside[x], UnitStep[x]"}, 
  PlotStyle -> Thickness[.015], ImageSize -> 270];
```

**Figure 3.6** The Heavyside function is the generalized unit stepfunction. It is the limiting case of the Error function for $\lim \sigma \to 0$.

The derivative of the Heavyside step function is the Delta function again:

```mathematica
D[UnitStep[x], x]
```

Output:
```
DiracDelta[x]
```

## 3.6 Separability

The Gaussian kernel for dimensions higher than one, say N, can be described as a regular product of N one-dimensional kernels. Example: $g_{2D}(x, y; \sigma_1^2 + \sigma_2^2) = g_{1D}(x; \sigma_1^2) \cdot g_{1D}(y; \sigma_2^2)$ where the space in between is the product operator. The regular product also explains the exponent N in the normalization constant for N-dimensional Gaussian kernels in (0). Because higher dimensional Gaussian kernels are regular products of one-dimensional Gaussians, they are called separable. We will use quite often this property of separability.

```mathematica
DisplayTogetherArray[{
  Plot[gauss[x, s = 1], {x, -3, 3}], 
  Plot3D[gauss[x, s = 1] gauss[y, s = 1], {x, -3, 3}, {y, -3, 3}]
}, ImageSize -> 440];
```

**Figure 3.7** A product of Gaussian functions gives a higher dimensional Gaussian function. This is a consequence of the separability.

An important application is the speed improvement when implementing numerical separable convolution. In chapter 5 we explain in detail how the convolution with a 2D (or better: N-dimensional) Gaussian kernel can be replaced by a cascade of 1D convolutions, making the process much more efficient because convolution with the 1D kernels requires far fewer multiplications.

## 3.7 Relation to binomial coefficients

Another place where the Gaussian function emerges is in expansions of powers of polynomials. Here is an example:

```mathematica
Expand[(x + y)^30]
```

Output:
```
x^30 + 30 x^29 y + 435 x^28 y^2 + 4060 x^27 y^3 + 27405 x^26 y^4 + 142506 x^25 y^5 +
593775 x^24 y^6 + 2035800 x^23 y^7 + 5852925 x^22 y^8 + 14307150 x^21 y^9 +
30045015 x^20 y^10 + 54627300 x^19 y^11 + 86493225 x^18 y^12 + 119759850 x^17 y^13 +
145422675 x^16 y^14 + 155117520 x^15 y^15 + 145422675 x^14 y^16 +
119759850 x^13 y^17 + 86493225 x^12 y^18 + 54627300 x^11 y^19 + 30045015 x^10 y^20 +
14307150 x^9 y^21 + 5852925 x^8 y^22 + 2035800 x^7 y^23 + 593775 x^6 y^24 +
142506 x^5 y^25 + 27405 x^4 y^26 + 4060 x^3 y^27 + 435 x^2 y^28 + 30 x y^29 + y^30
```

The coefficients of this expansion are the binomial coefficients $\binom{m}{n}$ ('n over m'):

```mathematica
ListPlot[Table[Binomial[30, n], {n, 1, 30}], 
  PlotStyle -> {PointSize[.015]}, AspectRatio -> .3];
```

**Figure 3.8** Binomial coefficients approximate a Gaussian distribution for increasing order.

And here in two dimensions:

```mathematica
BarChart3D[Table[Binomial[30, n] Binomial[30, m], {n, 1, 30}, {m, 1, 30}], 
  ImageSize -> 180];
```

**Figure 3.9** Binomial coefficients approximate a Gaussian distribution for increasing order. Here in 2 dimensions we see separability again.

## 3.8 The Fourier transform of the Gaussian kernel

We will regularly do our calculations in the Fourier domain, as this often turns out to be analytically convenient or computationally efficient. The basis functions of the Fourier transform $\mathcal{F}$ are the sinusoidal functions $e^{i\omega x}$. The definitions for the Fourier transform and its inverse are:

**the Fourier transform:**
$$F(\omega) = \mathcal{F}\{f(x)\} = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx$$

**the inverse Fourier transform:**
$$\mathcal{F}^{-1}\{F(\omega)\} = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} F(\omega) e^{-i\omega x} d\omega$$

```mathematica
s = .; 
Fgauss[w_, s_] = Simplify[
  1/Sqrt[2 Pi] Integrate[1/(s Sqrt[2 Pi]) Exp[-x^2/(2 s^2)] Exp[I w x], 
    {x, -Infinity, Infinity}], 
  {s > 0, Im[s] == 0}]
```

Output:
$$\frac{e^{-\frac{1}{2}\sigma^2 \omega^2}}{\sqrt{2\pi}}$$

The Fourier transform is a standard Mathematica command:

```mathematica
Simplify[FourierTransform[gauss[x, s], x, w], s > 0]
```

Output:
$$\frac{e^{-\frac{1}{2}\sigma^2 \omega^2}}{\sqrt{2\pi}}$$

Note that different communities (mathematicians, computer scientists, engineers) have different definitions for the Fourier transform. From the Mathematica help function:

> With the setting `FourierParameters->{a,b}` the discrete Fourier transform computed by `FourierTransform` is $\sqrt{\frac{|b|}{(2\pi)^{1-a}}} \int_{-\infty}^{\infty} f(t) e^{ib\omega t} dt$. Some common choices for {a,b} are {0,1} (default), {-1,1} (data analysis), {1,-1} (signal processing).

In this book we consistently use the default definition.

So the Fourier transform of the Gaussian function is again a Gaussian function, but now of the frequency $\omega$. The Gaussian function is the only function with this property. Note that the scale $\sigma$ now appears as a multiplication with the frequency. We recognize a well-known fact: a smaller kernel in the spatial domain gives a wider kernel in the Fourier domain, and vice versa. Here we plot 3 Gaussian kernels with their Fourier transform beneath each plot:

```mathematica
Block[{$DisplayFunction = Identity}, 
  p1 = Table[Plot[gauss[x, s], {x, -10, 10}, PlotRange -> All, 
    PlotLabel -> "gauss[x," <> ToString[s] <> "]"], {s, 1, 3}];
  p2 = Table[Plot[Fgauss[w, s], {w, -3, 3}, PlotRange -> All, 
    PlotLabel -> "Fgauss[x," <> ToString[s] <> "]"], {s, 1, 3}]
];
Show[GraphicsArray[{p1, p2}], ImageSize -> 400];
```

**Figure 3.10** Top row: Gaussian function at scales $\sigma=1$, $\sigma=2$ and $\sigma=3$. Bottom row: Fourier transform of the Gaussian function above it. Note that for wider Gaussian its Fourier transform gets narrower and vice versa, a well known phenomenon with the Fourier transform. Also note by checking the amplitudes that the kernel is normalized in the spatial domain only.

There are many names for the Fourier transform $\mathcal{F}g(\omega; \sigma)$ of $g(x; \sigma)$: when the kernel $g(x; \sigma)$ is considered to be the point spread function, $\mathcal{F}g(\omega; \sigma)$ is referred to as the modulation transfer function. When the kernel $g(x;\sigma)$ is considered to be a signal, $\mathcal{F}g(\omega; \sigma)$ is referred to as the spectrum. When applied to a signal, it operates as a lowpass filter. Let us plot the spectra of a series of such filters (with a logarithmic increase in scale) on double logarithmic paper:

```mathematica
scales = N[Table[Exp[t/3], {t, 0, 8}]]
spectra = LogLinearPlot[Fgauss[w, #], {w, .01, 10}, 
  DisplayFunction -> Identity] & /@ scales;
Show[spectra, DisplayFunction -> $DisplayFunction, AspectRatio -> .4, 
  PlotRange -> All, AxesLabel -> {"w", "Amplitude"}, ImageSize -> 300];
```

Output:
```
{1., 1.39561, 1.94773, 2.71828, 3.79367, 5.29449, 7.38906, 10.3123, 14.3919}
```

**Figure 3.11** Fourier spectra of the Gaussian kernel for an exponential range of scales $\sigma = 1$ (most right graph) to $\sigma = 14.39$ (most left graph). The frequency $\omega$ is on a logarithmic scale. The Gaussian kernels are seen to act as low-pass filters.

Due to this behaviour the role of receptive fields as lowpass filters has long persisted. But the retina does not measure a Fourier transform of the incoming image, as we will discuss in the chapters on the visual system (chapters 9-12).

## 3.9 Central limit theorem

We see in the paragraph above the relation with the central limit theorem: any repetitive operator goes in the limit to a Gaussian function. Later, when we study the discrete implementation of the Gaussian kernel and discrete sampled data, we will see the relation between interpolation schemes and the binomial coefficients. We study a repeated convolution of two blockfunctions with each other:

```mathematica
f[x_] := UnitStep[1/2 + x] + UnitStep[1/2 - x] - 1;
g[x_] := UnitStep[1/2 + x] + UnitStep[1/2 - x] - 1;
Plot[f[x], {x, -3, 3}, ImageSize -> 140];
```

**Figure 3.12** The analytical blockfunction is a combination of two Heavyside unitstep functions.

We calculate analytically the convolution integral:

```mathematica
h1 = Integrate[f[x] g[x - x1], {x, -Infinity, Infinity}]
```

Output:
```
1/2 (-1 + 2 UnitStep[1 - x1] - 2 x1 UnitStep[1 - x1] - 2 x1 UnitStep[x1]) +
1/2 (-1 + 2 x1 UnitStep[-x1] + 2 UnitStep[1 + x1] + 2 x1 UnitStep[1 + x1])
```

```mathematica
Plot[h1, {x1, -3, 3}, PlotRange -> All, ImageSize -> 150];
```

**Figure 3.13** One times a convolution of a blockfunction with the same blockfunction gives a triangle function.

The next convolution is this function convolved with the block function again:

```mathematica
h2 = Integrate[(h1 /. x1 -> x) g[x - x1], {x, -Infinity, Infinity}]
```

Output: [Complex expression with UnitStep functions]

We see that we get a result that begins to look more towards a Gaussian:

```mathematica
Plot[{h2, gauss[x1, .5]}, {x1, -3, 3}, PlotRange -> All, 
  PlotStyle -> {Dashing[{}], Dashing[{0.02, 0.02}]}, ImageSize -> 150];
```

**Figure 3.14** Two times a convolution of a blockfunction with the same blockfunction gives a function that rapidly begins to look like a Gaussian function. A Gaussian kernel with $\sigma = 0.5$ is drawn (dotted) for comparison.

The real Gaussian is reached when we apply an infinite number of these convolutions with the same function. It is remarkable that this result applies for the infinite repetition of any convolution kernel. This is the central limit theorem.

**Task 3.1** Show the central limit theorem in practice for a number of other arbitrary kernels.

## 3.10 Anisotropy

```mathematica
PlotGradientField[-gauss[x, 1] gauss[y, 1], 
  {x, -3, 3}, {y, -3, 3}, PlotPoints -> 20, ImageSize -> 140];
```

**Figure 3.15** The slope of an isotropic Gaussian function is indicated by arrows here. There are circularly symmetric, i.e. in all directions the same, from which the name isotropic derives. The arrows are in the direction of the normal of the intensity landscape, and are called gradient vectors.

The Gaussian kernel as specified above is isotropic, which means that the behaviour of the function is in any direction the same. For 2D this means the Gaussian function is circular, for 3D it looks like a fuzzy sphere.

It is of no use to speak of isotropy in 1-D. When the standard deviations in the different dimensions are not equal, we call the Gaussian function anisotropic. An example is the pointspreadfunction of an astigmatic eye, where differences in curvature of the cornea/lens in different directions occur. This show an anisotropic Gaussian with anisotropy ratio of 2 ($\sigma_x / \sigma_y = 2$):

```mathematica
Unprotect[gauss];
gauss[x_, y_, sx_, sy_] := 1/(2 Pi sx sy) Exp[-(x^2/(2 sx^2) + y^2/(2 sy^2))];
sx = 2; sy = 1; 
Block[{$DisplayFunction = Identity}, 
  p1 = DensityPlot[gauss[x, y, sx, sy], {x, -10, 10}, {y, -10, 10}, PlotPoints -> 50];
  p2 = Plot3D[gauss[x, y, sx, sy], {x, -10, 10}, {y, -10, 10}, Shading -> True];
  p3 = ContourPlot[gauss[x, y, sx, sy], {x, -5, 5}, {y, -10, 10}]
];
Show[GraphicsArray[{p1, p2, p3}], ImageSize -> 400];
```

**Figure 3.16** An anisotropic Gaussian kernel with anisotropy ratio $\sigma_x / \sigma_y = 2$ in three appearances. Left: DensityPlot, middle: Plot3D, right: ContourPlot.

## 3.11 The diffusion equation

The Gaussian function is the solution of several differential equations. It is the solution of $\frac{dy}{dx} = \frac{y(m-x)}{\sigma^2}$, because $\frac{dy}{y} = \frac{(m-x)}{\sigma^2} dx$, from which we find by integration $\ln(\frac{y}{y_0}) = -\frac{(m-x)^2}{2\sigma^2}$ and thus $y = y_0 e^{-\frac{(x-m)^2}{2\sigma^2}}$.

It is the solution of the linear diffusion equation, $\frac{\partial L}{\partial t} = \frac{\partial^2 L}{\partial x^2} + \frac{\partial^2 L}{\partial y^2} = \nabla L$.

This is a partial differential equation, stating that the first derivative of the (luminance) function $L(x, y)$ to the parameter t (time, or variance) is equal to the sum of the second order spatial derivatives. The right hand side is also known as the Laplacian (indicated by $\nabla$ for any dimension, we call $\nabla$ the Laplacian operator), or the trace of the Hessian matrix of second order derivatives:

```mathematica
hessian2D = {{Lxx, Lxy}, {Lxy, Lyy}}; 
Tr[hessian2D]
```

Output:
```
Lxx + Lyy
```

```mathematica
hessian3D = {{Lxx, Lxy, Lxz}, {Lyx, Lyy, Lyz}, {Lzx, Lyz, Lzz}}; 
Tr[hessian3D]
```

Output:
```
Lxx + Lyy + Lzz
```

The diffusion equation $\frac{\partial u}{\partial t} = \nabla u$ is one of some of the most famous differential equations in physics. It is often referred to as the heat equation. It belongs in the row of other famous equations like the Laplace equation $\nabla u = 0$, the wave equation $\frac{\partial^2 u}{\partial t^2} = \nabla u$ and the Schrödinger equation $\frac{\partial u}{\partial t} = i \nabla u$.

The diffusion equation $\frac{\partial u}{\partial t} = \nabla u$ is a linear equation. It consists of just linearly combined derivative terms, no nonlinear exponents or functions of derivatives.

The diffused entity is the intensity in the images. The role of time is taken by the variance $t = 2\sigma^2$. The intensity is diffused over time (in our case over scale) in all directions in the same way (this is called isotropic). E.g. in 3D one can think of the example of the intensity of an inkdrop in water, diffusing in all directions.

The diffusion equation can be derived from physical principles: the luminance can be considered a flow, that is pushed away from a certain location by a force equal to the gradient. The divergence of this gradient gives how much the total entity (luminance in our case) diminishes with time.

```mathematica
<< Calculus`VectorAnalysis`
SetCoordinates[Cartesian[x, y, z]];
Div[Grad[L[x, y, z]]]
```

Output:
```
L^(0,0,2)[x, y, z] + L^(0,2,0)[x, y, z] + L^(2,0,0)[x, y, z]
```

A very important feature of the diffusion process is that it satisfies a maximum principle [Hummel1987b]: the amplitude of local maxima are always decreasing when we go to coarser scale, and vice versa, the amplitude of local minima always increase for coarser scale. This argument was the principal reasoning in the derivation of the diffusion equation as the generating equation for scale-space by Koenderink [Koenderink1984a].

## 3.12 Summary of this chapter

The normalized Gaussian kernel has an area under the curve of unity, i.e. as a filter it does not multiply the operand with an accidental multiplication factor. Two Gaussian functions can be cascaded, i.e. applied consecutively, to give a Gaussian convolution result which is equivalent to a kernel with the variance equal to the sum of the variances of the constituting Gaussian kernels. The spatial parameter normalized over scale is called the dimensionless 'natural coordinate'.

The Gaussian kernel is the 'blurred version' of the Delta Dirac function, the cumulative Gaussian function is the Error function, which is the 'blurred version' of the Heavyside stepfunction. The Dirac and Heavyside functions are examples of generalized functions.

The Gaussian kernel appears as the limiting case of the Pascal Triangle of binomial coefficients in an expanded polynomial of high order. This is a special case of the central limit theorem. The central limit theorem states that any finite kernel, when repeatedly convolved with itself, leads to the Gaussian kernel.

Anisotropy of a Gaussian kernel means that the scales, or standard deviations, are different for the different dimensions. When they are the same in all directions, the kernel is called isotropic.

The Fourier transform of a Gaussian kernel acts as a low-pass filter for frequencies. The cut-off frequency depends on the scale of the Gaussian kernel. The Fourier transform has the same Gaussian shape. The Gaussian kernel is the only kernel for which the Fourier transform has the same shape.

The diffusion equation describes the expel of the flow of some quantity (intensity, temperature) over space under the force of a gradient. It is a second order parabolic differential equation. The linear, isotropic diffusion equation is the generating equation for a scale-space. In chapter 21 we will encounter a wealth on nonlinear diffusion equations.
