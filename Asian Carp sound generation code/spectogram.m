

%sound(data, fs, 16);
x = data(:,1);

Nw = 256;

  j = 1:Nw;
  w = 0.5*(1-cos(2*pi*(j-1)/Nw))'; % Hanning window of length Nw:
                                   % SP toolbox: w=hanning(Nw,'periodic')
  varw = 3/8; % Mean-square value of taper function w (used to
              % renormalize power spectrum).

  % Segment the data into 'full' and 'half' windows, arrayed in columns

  nwinf = floor(Ny/Nw); % Number of 'full' windows starting each Nw samples
  nwinh = nwinf - 1;    % Number of 'half' windows (half-way between fulls)
  nwin = nwinf+nwinh;

  yw = zeros(Nw,nwin);  % Define array in which to insert windowed data
  yw(:,1:2:nwin) = reshape(y(1:nwinf*Nw),Nw,nwinf);
  yw(:,2:2:(nwin-1)) = reshape(y((1+Nw/2):(nwinf-0.5)*Nw),Nw,nwinh);

  % Taper each column (i. e. the data in each window)

  wmx = repmat(w,[1 nwin]);
  yt = wmx.*yw;

  % DFT and power spectrum of each column

  ythat = fft(yt);
  S = (abs(ythat/Nw).^2)/varw; %Windowed power spectrum
  S = S(1:Nw/2,:);  % Only keep nonnegative harmonics for plotting
  SdB = 10*log10(S); % log of spectrum in decibel-like units
  Mw = 0:(Nw/2 - 1);  % Nonnegative windowed harmonics
  fw = Fs*Mw/Nw; % "Frequencies'(inverse periods in Hz) of these harmonics
  tw = (1:nwin)*0.5*Nw/Fs; % Center time of each window

  % Plot the power spectra (log or decibel scale) vs. window time

  subplot(2,1,2)

  % Add offsets and padding so pcolor centers each cell on (tw,fw)
  % and last row/col of field is included in plots
  dfw = fw(2)-fw(1);
  dtw = tw(2)-tw(1);
  fwpad = [fw fw(end)+dfw]-0.5*dfw;
  twpad = [tw tw(end)+dtw]-0.5*dtw;
  SdBpad = SdB([1:end end],[1:end end]);
  pcolor(twpad,fwpad,SdBpad)
  xlabel('time [s]')
  ylabel('Frequency [Hz]')
  title('Windowed spectral power of Messiah sample')
  shading flat
  colorbar